---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifyRecords.html
archived_at: '2026-07-15T07:23:40.484765Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Modifying Records (records/modify)

Apply multiple types of operations—such as creating, updating, replacing, and deleting records— to different records in a single request.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/records/modify`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. The possible values are:  |  |  | | --- | --- | | **`public`** | : The database that is accessible to all users of the app. | | **`private`** | : The database that contains private data that is visible only to the current user. | | **`shared`** | : The database that contains records shared with the current user. | |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `operations` | An array of dictionaries defining the operations to apply to records in the database. The dictionary keys are described in [Record Operation Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknltc). See [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi) for maximum number of operations allowed. This key is required. |
| `zoneID` | A dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `atomic` | A Boolean value indicating whether the entire operation fails when one or more operations fail.  If `true`, the entire request fails if one operation fails. If `false`, some operations may succeed and others may fail. The default value is `true`.  Note this property only applies to custom zones. |
| `desiredKeys` | An array of strings containing record field names that limit the amount of data returned in the enclosing operation dictionaries. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `numbersAsStrings` | A Boolean value indicating whether number fields should be represented by strings. The default value is `false`. |

### Record Operation Dictionary

The operation dictionary keys are:

| Key | Description |
| --- | --- |
| `operationType` | The type of operation. Possible values are described in [Operation Type Values](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknltk). This key is required. |
| `record` | A dictionary representing the record to modify, as described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). This key is required. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields.  This `desiredKeys` setting overrides the `desiredKeys` setting in the enclosing dictionary. |

### Operation Type Values

The possible values for the `operationType` key are:

| Value | Description |
| --- | --- |
| `create` | Create a new record. This operation fails if a record with the same record name already exists. |
| `update` | Update an existing record. Only the fields you specify are changed. |
| `forceUpdate` | Update an existing record regardless of conflicts. Creates a record if it doesn’t exist. |
| `replace` | Replace a record with the specified record. The fields whose values you do not specify are set to `null`. |
| `forceReplace` | Replace a record with the specified record regardless of conflicts. Creates a record if it doesn’t exist. |
| `delete` | Delete the specified record. |
| `forceDelete` | Delete the specified record regardless of conflicts. |

### Response

The response is an array of dictionaries describing the results of the operation. The dictionary contains a single key:

| Key | Description |
| --- | --- |
| `records` | An array containing a result dictionary for each operation in the request. If successful, the result dictionary contains the keys described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). If unsuccessful, the result dictionary contains the keys described in [Record Fetch Error Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlto). |

### Record Fetch Error Dictionary

The error dictionary describing a failed operation with the following keys:

| Key | Description |
| --- | --- |
| `recordName` | The name of the record that the operation failed on. |
| `reason` | A string indicating the reason for the error. |
| `serverErrorCode` | A string containing the code for the error that occurred. For possible values, see [Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc). |
| `retryAfter` | The suggested time to wait before trying this operation again. If this key is not set, the operation can’t be retried. |
| `uuid` | A unique identifier for this error. |
| `redirectURL` | A redirect URL for the user to securely sign in using their Apple ID. This key is present when `serverErrorCode` is `AUTHENTICATION_REQUIRED`. |

### Discussion

A request to modify records applies multiple types of operations to different types of records in a single request. Changes are saved to the database in a single operation. If the `atomic` key is `true` and one operation fails, the entire request fails. If the `atomic` key is `false`, some of the operations may succeed even when others fail. The operations are applied in the order in which they appear in the `operations` dictionary. One operation per record is allowed in the `operations` dictionary. The contents of an operation dictionary depends on the type of operation.

For example, to modify records in the Gallery app’s public database in the development environment, compose the URL as follows:

`https://apple-cloudkit.com/database/1/iCloud.com.example.gkumar.Gallery/development/public/records/modify`

Then, construct the request depending on the types of operations you want to apply.

### Creating the JSON Dictionary

Create a JSON dictionary representing the changes you want to make to multiple records in a database. For example, if you want to modify records in the default zone, simply include the operations key and insert the appropriate operation dictionary for the type of operation, described below.

1. `{`
2. `"operations" : [`
3. `// Insert Operation dictionaries in this array`
4. `],`
5. `}`

### Creating Records

To create a single record in the specified database, use the `create` operation type.

1. Create an operation dictionary with these key-value pairs:

   1. Set the `operationType` key to `create`.
   2. Set the `record` key to a record dictionary describing the new record.
2. Create a record dictionary with these key-value pairs:

   1. Set the `recordType` key to the record’s type.
   2. Set the `recordName` key to the record’s name.

      If you don’t provide a record name, CloudKit assigns one for you.
   3. Set the `fields` key to a dictionary of key-value pairs used to set the record’s fields, as described in [Record Field Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcna).

      The keys are the field names and the values are the initial values for the fields.
3. Add the operation dictionary to the `operations` array.

For example, this operation dictionary creates an `Artist` record with the first name “Mei” and last name “Chen”:

1. `{`
2. `"operationType" : "create",`
3. `"record" : {`
4. `"recordType" : "Artist",`
5. `"fields" : {`
6. `"firstName" : {"value" : "Mei"},`
7. `"lastName" : {"value" : "Chen"}`
8. `}`
9. `"recordName" : "Mei Chen"`
10. `},`
11. `}`

### Updating Records

To update the specified fields of an existing record, use the `update` or `forceUpdate` operation type.

1. Create an operation dictionary with these key-value pairs:

   1. Set the `operationType` key to `update` or `forceUpdate`.

      If you want the operation to fail when there is a conflict, use `update`; otherwise, use `forceUpdate`. The `forceUpdate` operation updates the record regardless of a conflict.
   2. Set the `record` key to a record dictionary describing the new field values.
2. Create a record dictionary with these key-value pairs:

   1. If `operationType` is `forceUpdate`, set the `recordType` key to the record’s type.
   2. Set the `recordName` key to the record’s name.
   3. Set the `fields` key to a dictionary of key-value pairs used to set the record’s fields.

      The keys are the field names and the values are the new values for the fields.
   4. If `operationType` is `update`, set the `recordChangeTag` key to the value of the existing record.
3. Add the operation dictionary to the `operations` array in the JSON dictionary.

For example, this operation dictionary changes the `width` and `height` fields of an existing `Artwork` record:

1. `{`
2. `"operationType" : "update",`
3. `"record" : {`
4. `"fields" : {`
5. `"width": {"value": 18},`
6. `"height": {"value": 24}`
7. `}`
8. `"recordName" : "101",`
9. `"recordChangeTag" : "e"`
10. `},`
11. `}`

### Replacing Records

To replace an entire record, use the `replace` or `forceReplace` operation type.

1. Create an operation dictionary with these key-value pairs:

   1. Set the `operationType` key to `replace` or `forceReplace`.

      If you want the operation to fail when there is a conflict, use `replace`; otherwise, use `forceReplace`.
   2. Set the `record` key to a record dictionary identifying the record to replace and containing the replacement record field values.
2. Create a record dictionary with these key-value pairs:

   1. Set the `recordName` key to the name of the record you want to replace.
   2. Set the `fields` key to a dictionary of key-value pairs used to set the replacement record’s fields. Fields that you omit from the dictionary are set to `null`.

      The keys are the field names and the values are the new values for the fields.
   3. If `operationType` is `replace`, set the `recordChangeTag` key to the value of the existing record.
3. Add the operation dictionary to the `operations` array.

### Deleting Records

To delete a record, use the `delete` or `forceDelete` operation type.

1. Create an operation dictionary with these key-value pairs:

   1. Set the `operationType` key to `delete` or `forceDelete`.

      If you want the operation to fail when there is a conflict, use `delete`; otherwise, use `forceDelete`.
   2. Set the `record` key to a record dictionary identifying the record to delete.
2. Create a record dictionary with a single key-value pair, whose key is `recordName`.
3. Add the operation dictionary to the `operations` array.

### Sharing Records

Shared records must have a short GUID. To create a record that will be shared, add the `createShortGUID` key to the record dictionary in the request when you create the record as in:

1. `{`
2. `"operations": [{`
3. `"operationType": "create",`
4. `"record": {`
5. `"recordName": "RecordA",`
6. `"recordType": "myType",`
7. `"createShortGUID": true`
8. `}`
9. `}],`
10. `"zoneID": {`
11. `"zoneName": "myCustomZone"`
12. `}`
13. `}`

In the response, the `shortGUID` key will be set in the record dictionary.

To share this record, create a record of type `cloudKit.share`. If the original record has no `shortGUID` key, one will be created for you. In the request, specify the public permissions and participants as in:

1. `{`
2. `"operations": [{`
3. `"operationType": "create",`
4. `"record": {`
5. `"recordType": "cloudKit.share",`
6. `"fields": {},`
7. `"forRecord": {`
8. `"recordName": "RecordA",`
9. `"recordChangeTag": "2"`
10. `},`
11. `"publicPermission": "NONE",`
12. `"participants": [{`
13. `"type": "USER",`
14. `"permission": "READ_WRITE",`
15. `"acceptanceStatus": "INVITED",`
16. `"userIdentity": {`
17. `"lookupInfo": {`
18. `"emailAddress": "gkumar@mac.com"`
19. `}`
20. `}`
21. `}]`
22. `}`
23. `}],`
24. `"zoneID": {`
25. `"zoneName": "myCustomZone"`
26. `}`
27. `}`

In the response, the record will have these keys set that are present only in a share, described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm):

- `shortGUID`
- `share`
- `publicPermission`
- `participants`
- `owner`
- `currentUserParticipant`

### Related Framework API

This request is similar to using the [CKModifyRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordsoperation) class in the CloudKit framework.

[Composing Web Service Requests](SettingUpWebServices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrufvjvomi)

[Fetching Records Using a Query (records/query)](QueryingRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnjnknlti)
