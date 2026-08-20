---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GettingAllZones.html
archived_at: '2026-07-15T07:23:36.893012Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Zones (zones/list)

This request fetches all the zones and their sync tokens in the specified database.

### Path

`GET [path]/database/[version]/[container]/[environment]/[database]/zones/list`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. Pass `public` to use the database that is accessible to all users of the app. Pass `private` to use the database that is visible only to the currently signed-in user. |

### Response

The response is a dictionary containing the results per zone with the following key:

| Key | Description |
| --- | --- |
| `zones` | An array containing a dictionary for each zone in the specified database. If successful, the dictionary contains the keys described in [Zone Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcma). If unsuccessful, the dictionary contains the keys described in [Zone Fetch Error Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomq). |

### Zone Fetch Error Dictionary

Dictionary describing a failed zone fetch with the following keys:

| Key | Description |
| --- | --- |
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `reason` | String indicating the reason for the error. |
| `serverErrorCode` | A string containing the code for the error that occurred. For possible values, see [Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc). |
| `retryAfter` | The suggested time to wait before trying this operation again. If this key is not set, the operation can’t be retried. |
| `redirectURL` | A redirect URL for the user to securely sign in using their Apple ID. This key is present when `serverErrorCode` is `AUTHENTICATION_REQUIRED`. |

### Related Framework API

This request is similar to using the [CKFetchRecordZonesOperation](https://developer.apple.com/documentation/cloudkit/ckfetchrecordzonesoperation) class in the CloudKit framework.

[Referencing Existing Assets (assets/rereference)](RereferenceAssets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqojnknltc)

[Fetching Zones by Identifier (zones/lookup)](GettingZonesbyIdentifier.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrsfvjvomi)
