---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/UploadAssets.html
archived_at: '2026-07-15T07:23:46.794552Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Uploading Assets (assets/upload)

Request tokens for asset fields in new or existing records used in another request to upload asset data.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/assets/upload`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. Pass `public` to use the database that is accessible to all users of the app. Pass `private` to use the database that is visible only to the currently signed-in user. |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). The default is the default zone. |
| `tokens` | An array of asset fields, described in [Asset Field Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqobnknlte). See [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi) for the maximum number of tokens allowed in this request. This key is required. |

### Asset Field Dictionary

Dictionary that identifies a field of type Asset in a record.

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. The default is a random UUID. |
| `recordType` | The name of the record type. |
| `fieldName` | The name of an Asset or Asset list field belonging to the record type. This key is required. |

### Response

An array of tokens containing the upload URLs. There’s one token dictionary, described in [Token Response Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqobnknltg), for each asset field specified in the request.

### Token Response Dictionary

Provides a URL for uploading an asset.

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. The default value is a random UUID. |
| `fieldName` | The name of a field belonging to the record type. |
| `url` | The location to upload the asset data. |

### Discussion

To set asset values, you request upload URLs for the asset fields of new and existing records. Upload URLs are valid for a limited time (15 minutes), and the maximum file size is 15 MB.

### Setting Asset Values in Records

Requesting URLs to upload asset data is just one step in the workflow to set asset values in records. The steps to set asset values are:

1. Request URLs for uploading asset data.
2. Upload the asset data.
3. Set the asset fields in records to the uploaded data.

### Request URLs

To request URLs to upload asset data, compose a request similar to:

1. `curl -X POST '[path]/database/[version]/[container]/[environment]/[database]/assets/upload' -H 'content-type: application/json' -d '{`
2. `"tokens":[{`
3. `"recordType":"Artwork",`
4. `"fieldName":"image"`
5. `}]`
6. `}'`

The response is:

1. `{`
2. `"tokens":[{`
3. `"recordName":"4c016e24-c397-4c9d-81d6-dee3e3a48bb0",`
4. `"fieldName":"image",`
5. `"url":[ASSET_UPLOAD_URL]`
6. `}]`
7. `}`

### Upload Asset Data

For each token dictionary in the response, upload the asset using a `curl` command similar to:

1. `curl -X POST $[ASSET_UPLOAD_URL] -d@[ASSET_FILE]`

The response is an asset dictionary, describe in [Asset Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltg), that you pass in a modify request.

1. `{`
2. `"singleFile" :{`
3. `"wrappingKey" : [WRAPPING_KEY],`
4. `"fileChecksum" : [SIGNATURE],`
5. `"receipt" : [RECEIPT],`
6. `"referenceChecksum" : [REFERENCE_CHECKSUM],`
7. `"size" : [SIZE]`
8. `}`
9. `}`

### Modify Records with Asset Fields

Modify the records, described in [Modifying Records (records/modify)](ModifyRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlts), setting the asset fields to the asset value dictionaries returned in the previous step. For example, create an Artist record setting the image asset to the uploaded file:

1. `curl -X POST '[path]/database/[version]/[container]/[environment]/[database]/records/modify' -H 'content-type: application/json' -d '{`
2. `"operations" :[{`
3. `"operationType" : "create",`
4. `"record" :{`
5. `"recordType" : "Artist",`
6. `"fields" :{`
7. `"title" : {"value" : "MacKerricher State Park"},`
8. `"artist" : {"value" : "Mei Chen"},`
9. `"image" : {`
10. `"value" : {`
11. `"wrappingKey" : [WRAPPING_KEY],`
12. `"fileChecksum" : [FILE_CHECKSUM],`
13. `"receipt" : [RECEIPT],`
14. `"referenceChecksum" : [REFERENCE_CHECKSUM],`
15. `"size": [SIZE]`
16. `}`
17. `}`
18. `},`
19. `"recordName": "4c016e24-c397-4c9d-81d6-dee3e3a48bb0",`
20. `"desiredKeys": []`
21. `}`
22. `}]`
23. `}'`

If successful, the response is:

1. `{`
2. `"records": [{`
3. `"recordName" : "4c016e24-c397-4c9d-81d6-dee3e3a48bb0",`
4. `"recordChangeTag" : "1e",`
5. `"created" : {`
6. `"timestamp" : 1422312944104,`
7. `"userRecordName" : "_9a065b60313a5937e75e03ed8e8f383d",`
8. `"deviceID" : "iCloud"`
9. `},`
10. `"modified" : {`
11. `"timestamp" : 1422312944104,`
12. `"userRecordName" : "_9a065b60313a5937e75e03ed8e8f383d",`
13. `"deviceID" : "iCloud"`
14. `}`
15. `}]`
16. `}`

[Accepting Share Records (records/accept)](AcceptingShareRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrzfvjvomi)

[Referencing Existing Assets (assets/rereference)](RereferenceAssets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqojnknltc)
