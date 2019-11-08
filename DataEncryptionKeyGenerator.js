const fs = require('fs');
const base64 = require('uuid-base64');
const mongodb = require('mongodb');
const { ClientEncryption } = require('mongodb-client-encryption')(mongodb);

const { MongoClient } = mongodb;

const connectionString = 'mongodb://localhost:27017';
const keyVaultNamespace = 'encryption.__keyVault';
const path = './master-key.txt';

let kmsProviders;

try {
  const data = fs.readFileSync(path);
  kmsProviders = {
    local: {
      key: data,
    },
  };
} catch(err) {
  console.error(err);
}

const client = new MongoClient(connectionString, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
});

async function DataEncryptionKeyGenerator() {
  try {
    await client.connect();
    const encryption = new ClientEncryption(client, {
      keyVaultNamespace,
      kmsProviders,
    });
    const key = encryption.createDataKey('local');
    const base64DataKeyId = key.toString('base64');
    const uuidDataKeyId = base64.decode(base64DataKeyId);
    console.log('DataKeyId [UUID]: ', uuidDataKeyId);
    console.log('DataKeyId [base64]: ', base64DataKeyId);
  } finally {
    await client.close();
  }
}
DataEncryptionKeyGenerator();
