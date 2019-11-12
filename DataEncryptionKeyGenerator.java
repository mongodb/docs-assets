package com.example.fle;

import java.io.FileInputStream;
import java.io.IOException;
import java.util.Arrays;
import java.util.Base64;
import java.util.HashMap;
import java.util.Map;

import org.bson.BsonBinary;

import com.mongodb.ClientEncryptionSettings;
import com.mongodb.ConnectionString;
import com.mongodb.MongoClientSettings;
import com.mongodb.client.model.vault.DataKeyOptions;
import com.mongodb.client.vault.ClientEncryption;
import com.mongodb.client.vault.ClientEncryptions;

/**
 * Client-side Field Level Encryption - Data Encryption Key Creator
 */
public class DataEncryptionKeyGenerator {

    public static void main(String[] args) {

        String path = "master-key.txt";

        byte[] localMasterKey = new byte[96];

        try (FileInputStream fis = new FileInputStream(path)) {
            fis.readNBytes(localMasterKey, 0, 96);
        } catch (Exception e) {
            e.printStackTrace();
        }

        String kmsProvider = "local";

        Map<String, Object> keyMap = new HashMap<String, Object>();
        keyMap.put("key",  localMasterKey);

        Map<String, Map<String, Object>> kmsProviders = new HashMap<String, Map<String, Object>>();
        kmsProviders.put(kmsProvider, keyMap);

        String connectionString = "mongodb://localhost:27017";
        String keyVaultNamespace = "encryption.__keyVault";

        ClientEncryptionSettings clientEncryptionSettings = ClientEncryptionSettings.builder()
                .keyVaultMongoClientSettings(MongoClientSettings.builder()
                        .applyConnectionString(new ConnectionString(connectionString))
                        .build())
                .keyVaultNamespace(keyVaultNamespace)
                .kmsProviders(kmsProviders)
                .build();

        ClientEncryption clientEncryption = ClientEncryptions.create(clientEncryptionSettings);
        BsonBinary dataKeyId = clientEncryption.createDataKey(kmsProvider, new DataKeyOptions());
        System.out.println("DataKeyId [UUID]: " + dataKeyId.asUuid());

        String base64DataKeyId = Base64.getEncoder().encodeToString(dataKeyId.getData());
        System.out.println("DataKeyId [base64]: " + base64DataKeyId);
    }
}
