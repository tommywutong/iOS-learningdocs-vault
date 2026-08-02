---
title: CloudKit Web Services Reference
apple_id: TP40015240
resource_type: Guide
platform: CloudKit JS
topic: Data Management
technology: null
published: '2016-06-13'
source_url: https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/CloudKitWebServicesReference/RegisterTokens.html
archived_at: '2026-07-15T07:23:42.963695Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [CloudKit Web Services Reference](index.md)



## Registering Tokens (tokens/register)

You can register a token with a specified Apple Push Notification services (APNs) environment.

### Path

`POST [path]/database/[version]/[container]/[environment]/tokens/register`

### Parameters

|  |  |
| --- | --- |
| **_path_** | : The URL to the CloudKit web service, which is `https://api.apple-cloudkit.com`. |
| **_version_** | : The protocol version—currently, 1. |
| **_container_** | : A unique identifier for the app’s container. The container ID begins with `iCloud.`. |
| **_environment_** | : The version of the app’s container. Pass `development` to use the environment that is not accessible by apps available on the store. Pass `production` to use the environment that is accessible by development apps and apps available on the store. |

### Request

The POST request is a JSON dictionary containing the following keys:

| Key | Description |
| --- | --- |
| `apnsEnvironment` | A string that specifies the APNs environment. To use the production environment, set this key to `"production"`. To use the development environment, set this key to `"development"`. This key is required. |
| `apnsToken` | A token you use to register to receive push notifications from other containers. This key is required. |

### Related Framework API

This request is similar to using the [registerForRemoteNotifications](https://developer.apple.com/documentation/uikit/uiapplication/1623078-registerforremotenotifications) method in the [UIApplication](https://developer.apple.com/documentation/uikit/uiapplication) class. In the native API, the token is handled for you by the CloudKit daemon.

[Creating APNs Tokens (tokens/create)](CreateTokens.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmjzfvjvomi)

[Types and Dictionaries](Types.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge2tenbqfvbuqmznknlte)
