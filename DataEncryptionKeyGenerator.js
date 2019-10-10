const fs = require('fs');
const base64 = require('uuid-base64');
const mongodb = require('mongodb');
const { ClientEncryption } = require('mongodb-client-encryption')(mongodb);

const { MongoClient } = mongodb;

const connectionString = 'mongodb://localhost:27017';
const keyVaultNamespace = 'encryption.__keyVault';
const path = './master-key.txt';

let kmsProviders;

fs.readFile(path, (err, data) => {
  if (err) throw err;
  kmsProviders = {
    local: {
      key: data,
    },
  };
});

function DataEncryptionKeyGenerator() {
  const client = new MongoClient(connectionString, {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  });

  client.connect()
    .then(() => {
      const encryption = new ClientEncryption(client, {
        keyVaultNamespace,
        kmsProviders,
      });

      encryption.createDataKey('local', (err, key) => {
        if (err) {
          console.error(err);
        } else {
          const base64DataKeyId = key.toString('base64');
          const uuidDataKeyId = base64.decode(base64DataKeyId);
          console.log('DataKeyId [UUID]: ', uuidDataKeyId);
          console.log('DataKeyId [base64]: ', base64DataKeyId);
        }
      });
    });
}

DataEncryptionKeyGenerator();
