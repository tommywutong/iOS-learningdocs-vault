---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifyZones.html
archived_at: '2026-07-15T07:23:41.461584Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Modifying Zones (zones/modify)

You can apply multiple operations—such as create and delete zones—to different zones in a single request.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/zones/modify`

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
| `operations` | Array of dictionaries defining the operations to apply to zones in the database. The dictionary keys are described in [Zone Operation Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjqfvjvony). This key is required. |

### Zone Operation Dictionary

The dictionary keys for an operation are:

| Key | Description |
| --- | --- |
| `operationType` | The type of operation. Possible values are either `create` or `delete`. This key is required. |
| `zone` | A dictionary representing the zone to modify. It has a single `zoneID` key, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). This key is required. |

### Response

The response is a dictionary containing the results per operation with the following key:

| Key | Description |
| --- | --- |
| `zones` | An array containing a result dictionary for each zone in the `zones` request array. If successful, the result dictionary contains the keys described in [Zone Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcma). If unsuccessful, the result dictionary contains the keys described in [Zone Fetch Error Dictionary](GettingAllZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomq). |

### Discussion

All operations are attempted and performed in the order they appear in the `operations` array in the request. Check the `zones` array in the response for which operations are successful. Only one operation is permitted per zone in the request.

### Related Framework API

This request is similar to using the [CKModifyRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckmodifyrecordzonesoperation) class in the CloudKit framework.

[Fetching Zones by Identifier (zones/lookup)](GettingZonesbyIdentifier.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrsfvjvomi)

[Fetching Database Changes (changes/database)](FetchingDatabaseChanges%28changeszone%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrvfvjvomi)
