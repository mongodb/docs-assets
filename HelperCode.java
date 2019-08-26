import org.json.*;

public class HelperCode {
    public static void main(String[] args) {
        System.out.println(getJSONSchema("<insert_your_key_here>"));
    }
    
    public static JSONObject getEncryptedField(String keyId, String chosenBsonType, Boolean isDeterministic){
        JSONObject binaryForKey = new JSONObject();
        binaryForKey.put("base64", keyId);
        binaryForKey.put("subType", "04");
        JSONObject binWrapper = new JSONObject();
        binWrapper.put("$binary", binaryForKey);

        JSONObject encryptedFieldWrap = new JSONObject();
        JSONObject encrypt = new JSONObject();

        encrypt.put("bsonType", chosenBsonType);
        if(isDeterministic){
            encrypt.put("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Deterministic");
        }else{
            encrypt.put("algorithm", "AEAD_AES_256_CBC_HMAC_SHA_512-Random");
        }
        encrypt.put("keyId", new JSONArray().put(binWrapper));
        encryptedFieldWrap.put("encrypt", encrypt);
        return encryptedFieldWrap;
    }
    public static JSONObject getStandardField(String chosenBsonType){
        JSONObject standardField = new JSONObject();
        standardField.put("bsonType", chosenBsonType);
        standardField.put("description", "must be a " + chosenBsonType + " and is required");
        return standardField;
    }
    public static String getJSONSchema(String keyId){
        JSONObject properties = new JSONObject();
        properties.put("name", getStandardField("string"));
        properties.put("ssn", getEncryptedField(keyId, "int", true)); // determin
        properties.put("bloodType", getEncryptedField(keyId, "string", false)); //random

        JSONObject insurance = new JSONObject();
        insurance.put("bsonType", "object");
        JSONObject insuranceProperties = new JSONObject();
            insuranceProperties.put("policyNumber", getEncryptedField(keyId, "int", true));
            insuranceProperties.put("provider", getStandardField("string"));
        insurance.put("properties", insuranceProperties);
        properties.put("insurance", insurance);

        JSONObject medicalRecords = getEncryptedField(keyId, "array", false);
        properties.put("medicalRecords",medicalRecords);

		JSONObject patientsSchema = new JSONObject();
		patientsSchema.put("properties", properties);
		patientsSchema.put("bsonType", "object");
        String patientsSchemaAsString = patientsSchema.toString();
		return patientsSchemaAsString;
    }
}