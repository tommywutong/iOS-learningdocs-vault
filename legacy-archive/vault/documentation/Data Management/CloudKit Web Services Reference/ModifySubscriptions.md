---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/ModifySubscriptions.html
archived_at: '2026-07-15T07:23:40.957672Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Modifying Subscriptions (subscriptions/modify)

You can create, update, and delete subscriptions.

### Path

`POST [path]/database/[version]/[container]/[environment]/[database]/subscriptions/modify`

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
| `operations` | An array of dictionaries defining the operations to apply to subscriptions in the database. The dictionary keys are described in [Subscription Operation Dictionary](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjyfvjvomq). See [Data Size Limits](PropertyMetrics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrtfvjvomi) for the maximum number of operations allowed. This key is required. |

### Subscription Operation Dictionary

The subscription operation dictionary keys are:

| Key | Description |
| --- | --- |
| `operationType` | The type of operation. Possible values are:   - `"create"` to create a new subscription. - `"update"` to change an existing subscription. - `"delete"` to delete a subscription.   This key is required. |
| `subscription` | The subscription to apply the operation to, described in [Subscription Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmq), with the following differences:   - If the `subscriptionType` key is `"zone"`, the `query`, the `zoneID`, `firesOn`, and `firesOnce` keys are omitted. - If the `subscriptionType` key is `"query"`, the `zoneWide` Boolean key is included. The default value for the `zoneWide` key is `true`.   This key is required. |

### Response

The response is a dictionary containing the results for each subscription with the following key:

| Key | Description |
| --- | --- |
| `subscriptions` | An array containing one dictionary for each subscription. If the operation was successful, the dictionary contains the subscription information, described in [Subscription Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmq). If the operation was unsuccessful, the dictionary is an error dictionary, described in [Subscription Fetch Error Dictionary](GetSubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjwfvjvomy). |

### Related Framework API

This request is similar to using the [CKModifySubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckmodifysubscriptionsoperation) class in the CloudKit framework.

[Fetching Users by Record Name (users/lookup/id)](LookupUsersbyID.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjvfvjvomi)

[Fetching Subscriptions (subscriptions/list)](GetSubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjwfvjvomi)
