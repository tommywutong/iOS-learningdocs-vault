---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/LookupUsersbyID.html
archived_at: '2026-07-15T07:23:39.955490Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Users by Record Name (users/lookup/id)

> [!NOTE]
> 

You can fetch discoverable users with the specified record names.

### Path

`POST [path]/database/[version]/[container]/[environment]/public/users/lookup/id`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |

### Request

The POST request is a JSON dictionary containing the following key:

| Key | Description |
| --- | --- |
| `users` | Array of dictionaries where each dictionary specifies a user and contains a single `userRecordName` key. |

### Response

The response is a dictionary containing the results of the operation with the following key:

| Key | Description |
| --- | --- |
| `users` | An array of user dictionaries, described in [User Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmi), but not including an `emailAddress` key. |

### Related Framework API

This request is similar to the [CKDiscoverUserInfosOperation](https://developer.apple.com/documentation/cloudkit/ckdiscoveruserinfosoperation) class in the CloudKit framework.

[Fetching Users by Email (users/lookup/email)](LookupUsersbyEmail.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjufvjvomi)

[Modifying Subscriptions (subscriptions/modify)](ModifySubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjyfvjvomi)
