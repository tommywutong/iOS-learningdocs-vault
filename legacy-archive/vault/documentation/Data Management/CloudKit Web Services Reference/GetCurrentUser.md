---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GetCurrentUser.html
archived_at: '2026-07-15T07:23:35.389426Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Current User (users/current)

> [!NOTE]
> 

You can get information about the user who is currently signed in.

### Path

`GET [path]/database/[version]/[container]/[environment]/public/users/current`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |

### Response

If the user is discoverable, this request returns the user’s name in a dictionary with the following keys:

| Key | Description |
| --- | --- |
| `userRecordName` | The name of the user record. |
| `firstName` | The user’s first name. |
| `lastName` | The user’s last name. |

### Discussion

Fetching current users returns the user ID and their name if they are discoverable.

[Discovering All User Identities (GET users/discover)](DiscoveringAllUserIdentities.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmzrfvjvomi)

[Fetching Contacts (users/lookup/contacts)](LookupContacts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjtfvjvomi)
