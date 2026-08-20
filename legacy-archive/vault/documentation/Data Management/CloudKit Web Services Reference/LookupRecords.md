---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/LookupRecords.html
archived_at: '2026-07-15T07:23:38.450101Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Records by Record Name (records/lookup)

You can fetch records by record name.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/records/lookup`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID should begin with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. The possible values are:  |  |  | | --- | --- | | **`public`** | : The database that is accessible to all users of the app. | | **`private`** | : The database that contains private data that is visible only to the current user. | | **`shared`** | : The database that contains records shared with the current user. | |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `records` | Array of record dictionaries, described in [Lookup Record Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnrnknltc), identifying the records to fetch. This key is required. |
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). The default is the database default zone. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `numbersAsStrings` | A Boolean value indicating whether number fields should be represented by strings. The default value is `false`. |

### Lookup Record Dictionary

The lookup record dictionary keys are:

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. This key is required. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |

### Response

An array of dictionaries describing the results of the operation. The dictionary contains a single key:

| Key | Description |
| --- | --- |
| records | An array containing a result dictionary for each record requested. If successful, the result dictionary contains the keys described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). If unsuccessful, the result dictionary contains the keys described in [Record Fetch Error Dictionary](ModifyRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlto). |

### Related Framework API

This request is similar to using the [CKFetchRecordsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordsoperation) class in the CloudKit framework.

[Fetching Records Using a Query (records/query)](QueryingRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnjnknlti)

[Fetching Record Changes (records/changes)](ChangeRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnznknltc)
