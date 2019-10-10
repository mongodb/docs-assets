from pymongo import MongoClient
from pymongo.encryption_options import AutoEncryptionOpts
from pymongo.encryption import ClientEncryption
import base64
from bson.codec_options import CodecOptions
import os
from bson.binary import (Binary,
                         JAVA_LEGACY,
                         STANDARD,
                         UUID_SUBTYPE)
import uuid                         

OPTS = CodecOptions(uuid_representation=STANDARD)
connection_string = "mongodb://localhost:27017"
key_vault_namespace = "encryption.keyvault"

path = "master-key.txt"
file_bytes = os.urandom(96).strip()
f = open(path, "wb")
f.write(file_bytes.strip())
f.close()

from bson import binary

path = "./master-key.txt";
local_master_key = binary.Binary(open(path, "rb").read(96))

kms_providers = {
  "local": {
    "key": local_master_key,
  },
}

def data_encryption_key_generator():
    fle_opts = AutoEncryptionOpts(
    kms_providers,
    key_vault_namespace,
    mongocryptd_bypass_spawn = True
    )

    client = MongoClient(
        connection_string,
        auto_encryption_opts = fle_opts
    )

    client_encryption = ClientEncryption(
        kms_providers,
        key_vault_namespace,
        client,
        OPTS
    )
    data_key = client_encryption.create_data_key("local")
    uuid_data_key_id = uuid.UUID(bytes=data_key)
    base_64_data_key_id = base64.b64encode(data_key)
    print("DataKeyId [UUID]: ", uuid_data_key_id)
    print("DataKeyId [base64]: ", base_64_data_key_id)

data_encryption_key_generator()