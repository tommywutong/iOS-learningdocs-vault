---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/GetSubscriptions.html
archived_at: '2026-07-15T07:23:35.896414Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Subscriptions (subscriptions/list)

You can fetch all the subscriptions in the specified database.

### Path

`GET [path]/database/[version]/[container]/[environment]/[database]/subscriptions/list`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |
| **_database_** | : The database to store the data within the container. Pass `public` to use the database that is accessible to all users of the app. Pass `private` to use the database that is visible only to the currently signed-in user. |

### Response

The response is a dictionary containing the results for each subscription with the following key:

| Key | Description |
| --- | --- |
| `subscriptions` | An array containing one dictionary for each subscription. If the fetch of a subscription was successful, the dictionary contains the subscription information, described in [Subscription Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmq). If the fetch of a subscription was unsuccessful, the dictionary is an error dictionary, described in [Subscription Fetch Error Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjwfvjvomy). This key is required. |

### Subscription Fetch Error Dictionary

This dictionary describes a failed subscription fetch with the following keys:

| Key | Description |
| --- | --- |
| `subscriptionID` | A string that is a unique identifier for the subscription. |
| `reason` | A string indicating the reason for the error. |
| `serverErrorCode` | A string containing the code for the error that occurred. For possible values, see [Error Codes](ErrorCodes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqnbnknltc). |
| `redirectURL` | A redirect URL for the user to securely sign in using their Apple ID. This key is present when `serverErrorCode` is `AUTHENTICATION_REQUIRED`. |

### Related Framework API

This request is similar to using the [CKFetchSubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation) class in the CloudKit framework.

[Modifying Subscriptions (subscriptions/modify)](ModifySubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjyfvjvomi)

[Fetching Subscriptions by Identifier (subscriptions/lookup)](LookupSubscriptionsbyID.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjxfvjvomi)
