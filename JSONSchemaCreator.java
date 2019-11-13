package com.example.fle;

import java.io.FileOutputStream;
import java.io.IOException;

import org.json.JSONArray;
import org.json.JSONObject;

public class JSONSchemaCreator {
    public static final String DETERMINISTIC_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic";
    public static final String RANDOM_ENCRYPTION_TYPE = "AEAD_AES_256_CBC_HMAC_SHA_512-Random";

    public static JSONObject buildEncryptedField(String keyId, String bsonType, Boolean isDeterministic) {
        return new JSONObject()
                .put("encrypt", new JSONObject()
                        .put("bsonType", bsonType)
                        .put("algorithm", (isDeterministic) ? DETERMINISTIC_ENCRYPTION_TYPE : RANDOM_ENCRYPTION_TYPE)
                        );
    }

    public static JSONObject buildEncryptMetadata(String keyId) {
        return new JSONObject()
                .put("keyId", new JSONArray()
                        .put(new JSONObject()
                                .put("$binary", new JSONObject()
                                        .put("base64", keyId)
                                        .put("subType",  "04")
                                        )
                                )
                        );
    }

    public static JSONObject createJSONSchema(String keyId) {
        return new JSONObject()
                .put("bsonType", "object")
                .put("encryptMetadata", buildEncryptMetadata(keyId))
                .put("properties", new JSONObject()
                        .put("ssn", buildEncryptedField(keyId, "int", true))
                        .put("bloodType", buildEncryptedField(keyId, "int", false))
                        .put("medicalRecords", buildEncryptedField(keyId, "array", false))
                        .put("insurance", new JSONObject()
                                .put("properties", new JSONObject()
                                        .put("policyNumber", buildEncryptedField(keyId, "int", true))
                                        )
                                )
                        );
    }


    public static void main(String[] args) {
        JSONObject schema = createJSONSchema("<paste_your_key_id_here>"); // replace the "paste_your_key_id_here" with your data key id

        String path = "fle-schema.json";
        try (FileOutputStream stream = new FileOutputStream(path)) {
            stream.write(schema.toString().getBytes());

        } catch (IOException e)  {
            e.printStackTrace();
        }

        System.out.println(schema);
    }
}
