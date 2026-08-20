---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/RereferenceAssets.html
archived_at: '2026-07-15T07:23:43.765938Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Referencing Existing Assets (assets/rereference)

You can add another reference to an existing asset.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/assets/rereference`

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
| `zoneID` | Dictionary that identifies a record zone in the database, described in [Zone ID Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlts). |
| `assets` | Array of asset fields, described in [Assets Field Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqojnknltg), to fetch. This key is required. |

### Assets Field Dictionary

Dictionary that identifies a field of type Asset in a record.

| Key | Description |
| --- | --- |
| `recordName` | The unique name used to identify the record within a zone. The default value is a random UUID. This key is required. |
| `fieldName` | The name of a field belonging to the record type. This key is required. |

### Response

The response contains an array of asset value dictionaries, described in [Asset Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltg). There’s one asset value for each asset field in the request.

### Discussion

Request an existing asset if you want to use it in another record. This request returns asset values that you can use to set asset fields in other records. Assets are deleted only when all references to it are removed.

[Uploading Assets (assets/upload)](UploadAssets.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqobnknltc)

[Fetching Zones (zones/list)](GettingAllZones.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrrfvjvomy)
