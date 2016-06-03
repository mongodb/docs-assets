===================================
MongoDB Driver Documentation Assets
===================================

The `restaurants.json <https://github.com/mongodb/docs-assets/blob/drivers/restaurants.json>`_ dataset contains 10 documents of the form:

.. code-block:: none

   {
     "_id" : <ObjectId>,
     "name" : <string>,
     "contact" : {
        "phone" : <string>
        "email" : <string>
        "location" : [ <longitude>, <latitude> ]
     },
     "stars" : int,
     "categories" : <array of strings>
     "grades" : <array of integers>,
   }

Import DataSet
--------------

**Note:** The MongoDB deployment to which you wish to import the data must be running.

#. Download and save the `restaurants.json <https://github.com/mongodb/docs-assets/blob/drivers/restaurants.json>`_ dataset.

#. In the terminal shell or command prompt, use ``mongoimport`` (or
   ``mongoimport.exe`` on Windows) to insert the documents. For example,
   the following ``mongoimport`` connects to a ``mongod`` instance running
   on localhost on port number ``27017``.

   .. code-block:: sh

      mongoimport --db test --collection restaurants --drop --file <path to saved file>

   **Note:** If ``mongoimport`` is not in your path, either update the path or specify the full path to the executable.
   
   To import to a MongoDB deployment running on a different host or
   port, specify ``--host`` and ``--port`` options in your `mongoimport`
   command. See `mongoimport
   <https://docs.mongodb.com/manual/reference/program/mongoimport/>`_
   for details on available options.
