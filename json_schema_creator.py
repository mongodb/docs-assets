def json_schema_creator(key_id):
    return {
        'bsonType': 'object',
        'encryptMetadata': {
            'keyId': key_id
        },
        'properties': {
        'insurance': {
            'bsonType': "object",
            'properties': {
            'policyNumber': {
                'encrypt': {
                'bsonType': "int",
                'algorithm': "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic"
                }
            }
            }
        },
        'medicalRecords': {
            'encrypt': {
                'bsonType': "array",
                'algorithm': "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
            }
        },
        'bloodType': {
            'encrypt': {
                'bsonType': "string",
                'algorithm': "AEAD_AES_256_CBC_HMAC_SHA_512-Random"
            }
        },
        'ssn': {
            'encrypt': {
            'bsonType': 'int',
            'algorithm': 'AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic',
            }
        },
        'mobile': {
            'encrypt': {
            'bsonType': 'string',
            'algorithm': 'AEAD_AES_256_CBC_HMAC_SHA_512-Random',
            }
        }
        }
    }


print(json_schema_creator("<paste_your_data_key_id>")) # replace the "paste_your_data_key_id" with your data key id

