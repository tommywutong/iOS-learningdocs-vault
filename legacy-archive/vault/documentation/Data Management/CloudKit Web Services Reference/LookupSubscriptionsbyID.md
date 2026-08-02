---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/LookupSubscriptionsbyID.html
archived_at: '2026-07-15T07:23:38.950193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Fetching Subscriptions by Identifier (subscriptions/lookup)

You can fetch subscriptions with the specified identifiers.

### Path

`POST [path]/database/[version]/[container]/[environment]/subscriptions/lookup`

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
| `subscriptions` | An array of dictionaries containing a single `subscriptionID` key. The value of the `subscriptionID` key is a string representation of a unique identifier for the subscription you want to fetch. This key is required. |

### Response

The response is a dictionary containing the results per subscription with the following key:

| Key | Description |
| --- | --- |
| `subscriptions` | An array of dictionaries, containing one dictionary for each subscription. If the fetch of a subscription was successful, the dictionary represents the subscription, described in [Subscription Dictionary](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknltcmq). If the fetch of a subscription was unsuccessful, the dictionary is an error dictionary, described in [Subscription Fetch Error Dictionary](GetSubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjwfvjvomy). |

### Related Framework API

This request is similar to the [CKFetchSubscriptionsOperation](https://developer.apple.com/documentation/cloudkit/ckfetchsubscriptionsoperation) class in the CloudKit framework.

[Fetching Subscriptions (subscriptions/list)](GetSubscriptions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjwfvjvomi)

[Creating APNs Tokens (tokens/create)](CreateTokens.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjzfvjvomi)
