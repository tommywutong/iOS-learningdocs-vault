---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ChangeRecords.html
archived_at: '2026-07-15T07:23:30.756832Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Record Changes (records/changes)

> [!NOTE]
> 

You can fetch records that changed since a specified sync token or since a zone was created.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/records/changes`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID should begin with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to fetch the records from. The possible values are:  |  |  | | --- | --- | | **`private`** | : The database that contains private data that is visible only to the current user. | | **`shared`** | : The database that contains records shared with the current user. | |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | A dictionary that identifies a custom zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). Fetching record changes is supported only for custom zones. This key is required. |
| `resultsLimit` | The maximum number of records to fetch. The default is the maximum number of records allowed in a request, described in [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi). |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `syncToken` | Identifies a point in the zone’s change history. The first time you get record changes, omit this key and if `moreComing` is `true` in the response, use the `syncToken` in the response in the next request until `moreComing` is `false`. Otherwise, get the current sync token by fetching a zone. |
| `numbersAsStrings` | A Boolean value indicating whether number fields should be represented by strings. The default value is `false`. |

### Response

The response is a dictionary containing the results with the following keys:

| Key | Description |
| --- | --- |
| `moreComing` | A Boolean value that indicates whether there are more changes to request. If `moreComing` is `true`, request more changes using the value of the included `syncToken` key. If `moreComing` is `false`, there are no more changes. |
| `records` | An array containing a record dictionary for each record requested. If successful, the record dictionary contains the keys described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). If unsuccessful, the result dictionary contains the keys described in [Record Fetch Error Dictionary](ModifyRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrnknlto). |
| `reverse` | A Boolean value that indicates whether the changes are returned in reverse order. If `true`, the changes are in reverse order; otherwise, they are not. |
| `syncToken` | A point in the zone’s change history. If `moreComing` is `true`, use this sync token in the next request until `moreComing` is `false`. |

### Discussion

Requests for records that have changed are allowed only in custom zones—the database is visible only to the current user by default.

### Related Framework API

This request is similar to the [CKFetchRecordChangesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordchangesoperation) class in the CloudKit framework.

[Fetching Records by Record Name (records/lookup)](LookupRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnrnknlte)

[Fetching Record Information (records/resolve)](FetchingRecordInformation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmryfvjvomi)
