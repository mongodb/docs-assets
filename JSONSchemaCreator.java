package com.example.fle;

import java.io.FileOutputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import org.bson.Document;

public class JSONSchemaCreator {
    public static final String DETERMINISTIC_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic";
    public static final String RANDOM_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Random";

    public static Document buildEncryptedField(String bsonType, Boolean isDeterministic) {
        return new Document().
                append("encrypt", new Document()
                        .append("bsonType", bsonType)
                        .append("algorithm",
                                (isDeterministic) ? DETERMINISTIC_ENCRYPTION_TYPE : RANDOM_ENCRYPTION_TYPE));
    }

    public static Document buildEncryptMetadata(String keyId) {
        List<Document> keyIds = new ArrayList<Document>();
        keyIds.add(new Document()
                .append("$binary", new Document()
                        .append("base64", keyId)
                        .append("subType", "04")));
        return new Document().append("keyId", keyIds);
    }

    public static Document createJSONSchema(String keyId) {
        return new Document().append("bsonType", "object").append("encryptMetadata", buildEncryptMetadata(keyId))
                .append("properties", new Document()
                        .append("ssn", buildEncryptedField("int", true))
                        .append("bloodType", buildEncryptedField("string", false))
                        .append("medicalRecords", buildEncryptedField("array", false))
                        .append("insurance", new Document()
                                .append("bsonType", "object")
                                .append("properties",
                                        new Document().append("policyNumber", buildEncryptedField("int", true)))));
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
