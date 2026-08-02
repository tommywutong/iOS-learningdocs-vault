---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/FetchCurrentUserIdentity.html
archived_at: '2026-07-15T07:23:33.255362Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Current User Identity (users/caller)

Fetches information about the current user.

### Path

`GET [path]/database/[version]/[container]/[environment]/public/users/caller`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |

### Response

Dictionary containing the results of the operation with the following keys:

| Key | Description |
| --- | --- |
| `users` | Array containing one user identity dictionary representing the current user, described in [User Identity Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltemy). |

[Fetching Zone Changes (zones/changes)](GetZoneChanges.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjrfvjvomi)

[Discovering User Identities (POST users/discover)](DiscoveringUserIdentities%28usersdiscover%29.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmzqfvjvomi)
