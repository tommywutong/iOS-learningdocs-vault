---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/FetchingRecordZoneChanges(changeszone).html
archived_at: '2026-07-15T07:23:35.134815Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Record Zone Changes (changes/zone)

Fetches changed records in the specified zones.

> [!NOTE]
> 

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/changes/zone`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. The possible values are:  |  |  | | --- | --- | | **`private`** | : The database that contains private data that is visible only to the current user. | | **`shared`** | : The database that contains records shared with the current user. | |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `zones` | An array containing a _zone dictionary_ for each zone you want to fetch records from. A zone dictionary contains all the same keys as this request except `zones`, and a required `zoneID` key that identifies the zone. The values in the dictionary apply to the specific zone and overwrite the values in this request.  This key is required. |
| `reverse` | A Boolean value that indicates whether the changes are returned in reverse order. If `true`, the changes are in reverse order; otherwise, they are not. |
| `desiredKeys` | An array of strings containing record field names that limits the amount of data returned in this operation. Only the fields specified in the array are returned. The default is `null`, which fetches all record fields. |
| `numberAsStrings` | A Boolean value indicating whether number fields should be represented by strings. The default value is `false`. |
| `resultsLimit` | The maximum number of records to fetch. The default is the maximum number of records allowed in a request, described in [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi). |
| `desiredRecordTypes` | An array of record names that limit the amount of data returned in this operation. Only the changed records from the record types in the array are returned. The default is `null`, which fetches changes from all record types. |

### Response

Dictionary containing the results of the operation with the following keys:

| Key | Description |
| --- | --- |
| `zones` | An array containing a result dictionary for each zone in the request. If successful, the result dictionary contains the keys described in [Zone Record Fetch Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrwfvjvomq). If unsuccessful, the result dictionary contains the keys described in [Zone Record Fetch Error Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrwfvjvomy). |

### Zone Record Fetch Dictionary

The dictionary with fetched records from a zone with the following keys:

| Key | Description |
| --- | --- |
| `syncToken` | Identifies a point in the database’s change history. |
| `records` | An array containing a record dictionary for each record that changed in this zone, described in [Record Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltm). |
| `moreComing` | A Boolean value that indicates whether there are more changes to request. If `moreComing` is `true`, request more changes using the value of the included `syncToken` key. If `moreComing` is `false`, there are no more changes. |
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |

### Zone Record Fetch Error Dictionary

The dictionary describing a failed fetch with the following keys:

| Key | Description |
| --- | --- |
| `reason` | A string indicating the reason for the error. |
| `serverErrorCode` | A string containing the code for the error that occurred. For possible values, see [Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc). |
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |

[Fetching Database Changes (changes/database)](FetchingDatabaseChanges%28changeszone%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrvfvjvomi)

[Fetching Zone Changes (zones/changes)](GetZoneChanges.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjrfvjvomi)
