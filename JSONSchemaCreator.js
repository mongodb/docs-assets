function JSONSchemaCreator(keyId) {
  return {
    bsonType: 'object',
    encryptMetadata: {
      keyId,
    },
    properties: {
      insurance: {
        bsonType: 'object',
        properties: {
          policyNumber: {
            encrypt: {
              bsonType: 'int',
              algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic',
            },
          },
        },
      },
      medicalRecords: {
        encrypt: {
          bsonType: 'array',
          algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Random',
        },
      },
      bloodType: {
        encrypt: {
          bsonType: 'string',
          algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Random',
        },
      },
      ssn: {
        encrypt: {
          bsonType: 'int',
          algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic',
        },
      },
      mobile: {
        encrypt: {
          bsonType: 'string',
          algorithm: 'AEAD_AES_256_CBC_HMAC_SHA_512-Random',
        },
      },
    },
  };
}

const patientSchema = JSONSchemaCreator('<paste_your_key_id_here>'); // replace the "paste_your_key_id_here" with your data key id
console.log(JSON.stringify(patientSchema));
