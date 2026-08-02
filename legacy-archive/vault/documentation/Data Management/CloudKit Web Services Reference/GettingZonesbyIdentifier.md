---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GettingZonesbyIdentifier.html
archived_at: '2026-07-15T07:23:37.696196Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Zones by Identifier (zones/lookup)

You can fetch zones by using specified identifiers.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/zones/lookup`

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
| `zones` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). Use the `zoneName` key to specify the zone’s identifier. This key is required. |

### Response

The response is a dictionary containing the results per zone with the following key:

| Key | Description |
| --- | --- |
| `zones` | An array containing a result dictionary for each zone in the `zones` request array. If successful, the result dictionary contains the keys described in [Zone Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcma). If unsuccessful, the result dictionary contains the keys described in [Zone Fetch Error Dictionary](GettingAllZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomq). |

### Related Framework API

This request is similar to using the [CKFetchRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation) class in the CloudKit framework.

[Fetching Zones (zones/list)](GettingAllZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomy)

[Modifying Zones (zones/modify)](ModifyZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjqfvjvomi)
