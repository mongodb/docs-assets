const mongodb = require('mongodb');
const fs = require('fs');
const { ClientEncryption } = require('mongodb-client-encryption')(mongodb);
const { MongoClient } = mongodb;
const dotenv = require('dotenv');
dotenv.config();

const keyVaultNamespace = "encryption.__keyVault";
let kmsProviders;

// READ DATA FROM Master Key
const path = "./master-key.txt";
fs.readFile(path, (err, data) => {
  if (err) throw err;
  kmsProviders = {
    local: {
      key: data
    }
  }
});

function DataEncryptionKeyGenerator(){
    const client = new MongoClient(process.env.MONGO_URL, {
        useNewUrlParser: true,
        useUnifiedTopology: true
    });

    client.connect()
    .then((clientConnection)=>{
        const encryption = new ClientEncryption(client, {
            keyVaultNamespace,
            kmsProviders
        });

        encryption.createDataKey('local', (err, key) => {
            if (err) {
              console.log("dataKey creation error: \t", err);
            } else {
              // key creation succeeded
              console.log("dataKey created: \t", key)
            }
        })
    });
}
DataEncryptionKeyGenerator();
