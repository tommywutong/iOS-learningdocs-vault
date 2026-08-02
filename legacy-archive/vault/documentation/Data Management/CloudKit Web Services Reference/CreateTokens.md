---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/CreateTokens.html
archived_at: '2026-07-15T07:23:31.246696Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Creating APNs Tokens (tokens/create)

You can get a token that can be used to long-poll for push notifications from other containers. These tokens are known as Apple Push Notification services (APNs) tokens.

### Path

`POST [path]/database/[version]/[container]/[environment]/tokens/create`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |

### Request

The POST request is a JSON dictionary containing a single `apnsEnvironment` key that specifies the APNs environment. To use the production environment, set the key to `"production"`. To use the development environment, set the key to `"development"`.

### Response

The response dictionary contains the token information with the following keys:

| Key | Description |
| --- | --- |
| `apnsEnvironment` | The APNs environment specified in the request. |
| `apnsToken` | A token you use to register to receive push notifications from other instances of this app. |
| `webcourierURL` | The URL to use to long-poll for push notifications. |

[Fetching Subscriptions by Identifier (subscriptions/lookup)](LookupSubscriptionsbyID.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjxfvjvomi)

[Registering Tokens (tokens/register)](RegisterTokens.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmrqfvjvomi)
