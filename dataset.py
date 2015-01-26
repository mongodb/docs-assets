import copy
import tarfile
import os.path
import sys
import csv
import logging
import json
import urllib
import urllib2
import datetime
import time
import random
import bson.json_util
import bson
import threading
import multiprocessing

from giza.tools.timing import Timer
from giza.core.app import BuildApp
from giza.core.task import Task, check_dependency
from giza.config.base import ConfigurationBase

logger = logging.getLogger("dataset")
logging.basicConfig(level=logging.INFO)

########## Geolocation Coordination ##########

class Condition(object):
    def __init__(self):
        self._limited = None
        self.lock = threading.Lock()

    @property
    def limited(self):
        return self._limited

    @limited.setter
    def limited(self, value):
        with self.lock:
            self._limited = value

def get_coordinates(key, number, street, zip, cond, sleep=True):
    addr_string = ' '.join([number, street, zip])
    address = urllib.quote_plus(addr_string)

    url = "https://maps.googleapis.com/maps/api/geocode/json?address={0}".format(address)

    if cond.limited is True:
        return '_', {}
    elif cond.limited is False:
        if random.random() > 0.5:
            logger.info('hitting per-minute rate limiting, breathing')
        time.sleep(2)

    try:
        response = json.loads(urllib2.urlopen(url).read())
        logger.info('got coordinates for: {0}, ({1})'.format(addr_string, key))
    except urllib2.HTTPError as e:
        if e.code == 500:
            logger.warning('server issue, continuing.')
        elif e.code == 403:
            logger.error('encountered request error, terminating gracefully')
            cond.limited = True
        else:
            logger.error('encountered request error, continuing cautiously')
        return '_', {}
    except:
        logger.error("({0}): {1}".format(type(e), e))


    if response['status'] == 'OVER_QUERY_LIMIT':
        cond.limited = False
        if response['error_message'] == "You have exceeded your daily request quota for this API.":
            cond.limited = True
            if random.random() > 0.5:
                logger.info('hitting daily rate limiting')
            return '_', {}
        else:
            if cond.limited is False:
                return '_', {}
            else:
                cond.limited = False
                return get_coordinates(key, number,street, zip, cond, sleep)
    else:
        result = response['results'][0]

        return key, { "address": result['formatted_address'],
                      "lat": result['geometry']['location']['lat'],
                      "long": result['geometry']['location']['lng'] }

def cached_geo_resolution(mapping, cache, app):
    cond = Condition()

    count = 0
    for key, doc in mapping.items():
        if count > 2500:
            break
        if key not in cache:
            count += 1
            if app is None:
                key, cache[key] = get_coordinates(key, doc['address']['building'],
                                                  doc['address']['street'],
                                                  doc['address']['zipcode'], cond, True)
            else:
                app.add(Task(job=get_coordinates,
                             args=(key, doc['address']['building'],
                                   doc['address']['street'],
                                   doc['address']['zipcode'], cond, True),
                              target=True,
                              dependency=None))

    if app is not None and len(app.queue) > 0:
        logger.info('starting geo cache update. There are {0} jobs in the queue'.format(str(len(app.queue))))
        with Timer('running geo coordinate cache update'):
            try:
                cache_results = app.run()
                cache_results = dict(cache_results)
                if '_' in cache_results:
                    del cache_results['_']
                cache.update(cache_results)
                app.reset()
            except IndexError:
                logger.error('geocoding resolution did not yield new data')

    if len(cache) == len(mapping) or cond.limited is not True:
        logger.info('geocode cache is populated. continuing to update the dataset.')
    elif cond.limited is True:
        logger.info('hit daily geocoding api limit. cache may be incomplete. updating dataset')
    else:
        logger.info('hit temporary geocoding limit. cache may be incomplete. updating dataset')

    for key, doc in mapping.items():
        if len(mapping[key]['address']['coord']) == 0:
            if key not in cache:
                logger.debug('missing geo-coordinates for: ' + str(key))
            else:
                mapping[key]['address']['coord'] = [ cache[key]['long'], cache[key]['lat'] ]
        else:
            logger.debug('geocoordinates exist for ({0})'.format(key))

    logger.info("there are {0} records without geocoding".format(str(len(mapping) - len(cache))))
    return mapping, cache

########## Data Ingestion, Cleanup, and Formatting ##########

def clean_document(row):
    d = {
        'restaurant_id': row['CAMIS'],
        'name': row['DBA'].title(),
        'cuisine': row['CUISINE DESCRIPTION'],
        'borough': row['BORO'].title(),
        'address': {
            'building': row['BUILDING'].strip(),
            'street': row['STREET'].strip().title(),
            'zipcode': row['ZIPCODE'],
            'coord': []
        },
        'grades': []
    }

    if row['GRADE'] != "":
        try:
            month, day, year = row['GRADE DATE'].split('/')
        except ValueError:
            month, day, year = row['RECORD DATE'].split('/')

        try:
            score = int(row['SCORE'])
        except ValueError:
            if row['SCORE'] == '':
                score = None
            else:
                print(row)
                exit(1)

        grade_date = datetime.datetime(int(year), int(month), int(day))

        grade = {
            "score":  score,
            "grade": row['GRADE'],
            "date": grade_date
        }
    else:
        grade = {}

    return d, grade

def ingest_data(fn):
    mapping = {}

    logger.info('reading data from csv file: ' + fn)
    with open(fn, 'r') as f:
        reader = csv.DictReader(f)
        for num, row in enumerate(reader):
            row, grade = clean_document(row)

            rid = row['restaurant_id']
            if rid not in mapping:
                mapping[rid] = row

            if grade != {}:
                mapping[rid]['grades'].append(grade)

            logger.debug('now {0} grades in {1} record'.format(len(mapping[rid]['grades']), row['name']))

    return mapping

def reload_data(json_file):
    mapping = {}
    logger.info('reading data from json export file')

    with open(json_file, 'r') as f:
        for line in f.readlines():
            document = json.loads(line)
            rid = document['restaurant_id']

            for grade in document['grades']:
                grade['date'] = bson.EPOCH_AWARE + datetime.timedelta(seconds=float(grade['date']['$date'])/1000.0)

            mapping[rid] = document

    return mapping

def import_data(csv_file, json_file):
    if not os.path.isfile(json_file) or check_dependency(json_file, csv_file):
        return ingest_data(fn)
    else:
        pass

########## Output Generation ##########

def json_date_cleanup(mapping):
    for doc in mapping.values():
        for grade in doc['grades']:
            grade['date'] = bson.json_util.default(grade['date'])

    return mapping

def export_json_data(json_fn, mapping):
    # just be consistent for py3 standards:
    data_to_export = [ doc for doc in mapping.values() ]
    data_to_export.sort(key=lambda x: x['restaurant_id'])

    with open(json_fn, 'w') as jsonf:
        for doc in data_to_export:
            for grade in doc['grades']:
                grade['date'] = bson.json_util.default(grade['date'])

            json.dump(doc, jsonf, sort_keys=True)
            jsonf.write('\n')

    logger.info('wrote {0} export file'.format(json_fn))

def export_bson_data(bson_fn, mapping):
    with open(bson_fn, 'w') as bsonf:
        for doc in mapping.values():
            bsonf.write(bson.BSON.encode(doc))

    logger.info('wrote {0} export file'.format(bson_fn))

def create_tarball(dirname, files, fn):
    basename = dirname.split('.')[0]

    with tarfile.open(fn, 'w:gz') as tar:
        for f in files:
            if f.startswith(basename) and not f.endswith('.tar.gz'):
                tar.add(f, arcname=os.path.join(dirname, f))

    logger.info('created tarball: ' + fn)

########## Program Logic ##########

def data_set_tasks(basename, app):
    csv_fn = basename + '.csv'

    geo_coord_cache_fn = basename + ".geo-coord-cache.json"

    tar_deps = [csv_fn]
    export_deps = [csv_fn]

    with Timer('data ingestion'):
        ingest_app = app.add('app')
        ingest_app.add(Task(job=reload_data,
                            args="dataset.json",
                            target=None,
                            dependency=csv_fn))
        mapping = ingest_app.run()[0]
        logger.info("loaded {0} records".format(len(mapping)))
        app.reset()

    with ConfigurationBase.persisting(geo_coord_cache_fn, override=True) as geo_coord_cache:
        old_state = copy.copy(geo_coord_cache.state)
        with Timer("geocoding records"):
            mapping, cache = cached_geo_resolution(mapping, geo_coord_cache.state, app)
            logger.info('{0} items in the geocode cache'.format(len(cache)))
        if cache != old_state:
            export_deps.append(geo_coord_cache_fn)
            tar_deps.append(geo_coord_cache_fn)
            logger.info('changes detected in geocoding cache')
        else:
            logger.info('geocoding cache is unchanged in this run')

    export_app = app.add('app')
    for ext, func in [('bson', export_bson_data), ('json', export_json_data)]:
        fn = '.'.join((basename, ext))
        tar_deps.append(fn)
        export_app.add(Task(job=func,
                            args=(fn, mapping),
                            target=fn,
                            dependency=export_deps))

    tar_dirname = basename + '.' + str(datetime.date.today())
    tar_fn = tar_dirname + '.tar.gz'
    app.add(Task(job=create_tarball,
                 args=[tar_dirname, tar_deps, tar_fn],
                 target=tar_fn,
                 dependency=tar_deps))

def main(basename):
    with BuildApp.context() as app:
        app.pool = 'thread'

        data_set_tasks(basename, app)

    logger.info('data set manipulation complete')

if __name__ == '__main__':
    try:
        basename = os.path.splitext(sys.argv[1])[0]
    except IndexError:
        basename = 'dataset'

    main(basename)
