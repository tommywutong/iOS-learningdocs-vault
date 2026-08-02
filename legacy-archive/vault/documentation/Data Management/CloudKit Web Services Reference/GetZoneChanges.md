---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GetZoneChanges.html
archived_at: '2026-07-15T07:23:36.395697Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Zone Changes (zones/changes)

> [!NOTE]
> 

Returns the zones that changed since a specified sync token.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/zones/changes`

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
| `metaSyncToken` | Identifies a point in the zone’s change history. |
| `resultsLimit` | The maximum number of records to fetch. The default is the maximum number of records allowed in a request, described in [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi). |

### Response

Dictionary containing the results of the operation with the following keys:

| Key | Description |
| --- | --- |
| `zones` | An array containing a result dictionary for each zone in the specified database. If successful, the result dictionary contains the keys described in [Zone Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcma). If unsuccessful, the result dictionary contains the keys described in [Zone Fetch Error Dictionary](GettingAllZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomq). |
| `metaSyncToken` | Identifies a point in the zone’s change history. |
| `moreComing` | Boolean value that indicates whether there are more changes to request. If `moreComing` is `true`, request more changes using the value of the included `syncToken` key. If `moreComing` is `false`, there are no more changes. |

### Discussion

Alternatively, you can get record changes for all the zones, as described in [Fetching Record Changes (records/changes)](ChangeRecords.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnznknltc).

[Fetching Record Zone Changes (changes/zone)](FetchingRecordZoneChanges%28changeszone%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrwfvjvomi)

[Fetching Current User Identity (users/caller)](FetchCurrentUserIdentity.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrxfvjvomi)
