package com.example.fle;

import java.io.FileOutputStream;
import java.io.IOException;

import com.mongodb.BasicDBList;
import com.mongodb.BasicDBObject;
import com.mongodb.DBObject;

public class JSONSChemaCreator {
    public static final String DETERMINISTIC_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic";
    public static final String RANDOM_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Random";

    public static DBObject buildEncryptedField(String keyId, String bsonType, Boolean isDeterministic) {
        return new BasicDBObject().
                append("encrypt", new BasicDBObject()
                        .append("bsonType", bsonType)
                        .append("algorithm",
                                (isDeterministic) ? DETERMINISTIC_ENCRYPTION_TYPE : RANDOM_ENCRYPTION_TYPE));
    }

    public static DBObject buildEncryptMetadata(String keyId) {
        BasicDBList keyIds = new BasicDBList();
        keyIds.add(new BasicDBObject()
                .append("$binary", new BasicDBObject()
                        .append("base64", keyId)
                        .append("subType", "04")));
        return new BasicDBObject().append("keyId", keyIds);
    }

    public static DBObject createJSONSchema(String keyId) {
        return new BasicDBObject().append("bsonType", "object").append("encryptMetadata", buildEncryptMetadata(keyId))
                .append("properties", new BasicDBObject()
                        .append("ssn", buildEncryptedField(keyId, "int", true))
                        .append("bloodType", buildEncryptedField(keyId, "string", false))
                        .append("medicalRecords", buildEncryptedField(keyId, "array", false))
                        .append("insurance", new BasicDBObject()
                                .append("bsonType", "object")
                                .append("properties",
                                        new BasicDBObject().append("policyNumber", buildEncryptedField(keyId, "int", true)))));
    }

    public static void main(String[] args) throws IOException {
        String schema = createJSONSchema("<your_key_id>").toString(); // replace "your_key_id" with your base64 data encryption key id

        String path = "fle-schema.json";
        try (FileOutputStream stream = new FileOutputStream(path)) {
            stream.write(schema.getBytes());
        }

        System.out.println(schema);
    }
}

