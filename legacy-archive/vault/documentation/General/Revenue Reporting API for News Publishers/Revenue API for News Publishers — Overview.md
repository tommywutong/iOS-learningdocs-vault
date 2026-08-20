---
title: Revenue Reporting API for News Publishers
apple_id: TP40016970
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iAd_News_Revenue_API/Document/Revenue_Ch1_Overview.html
archived_at: '2026-07-15T07:34:29.561947Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Summary%20of%20Revenue%20API%20for%20News%20Publishers%20Methods.md)

# Revenue API for News Publishers — Overview

Apple News publications monetize their available ad-placement inventory in two ways:

- Via _direct-sold_ campaigns.
- By turning on iAd _backfill_ which allows iAd-sold campaigns to be served within the publication’s available ad-placement inventory.

The iAd [Workbench for News Publishers](https://iadworkbench.apple.com/) lets you manage how your publications are being monetized, managing your direct-sold campaigns and turning on backfill, and also provides a breakdown of revenue by channel. The iAd Workbench is a web-based, interactive tool and the Revenue API for News Publishers provides programmatic access to the same data.

The Revenue API for News Publishers described in this document provides programmatic access to the iAd ad server, where you can use your own tools and programs to do the same kinds of tasks as you would do with the iAd Workbench:

- Obtain revenue performance metrics by channel.
- Obtain revenue performance metrics by creative (ad) type.

The Revenue API for News Publishers is available to all Apple News publisher accounts that have access to News Publisher tools on [iAd Workbench](https://iadworkbench.apple.com/).

Client side SSL certificate is used to authenticate the user. An access token provides authorization to all of the API.

To access the iAd server, you can request and download the required API keys, tokens, and certificates from the [iAd Workbench](https://iadworkbench.apple.com/) site.

1. Click on the dropdown arrow next to your account name near the top right and choosing Account from the dropdown menu.
2. Select the API tab under the page title.
3. Click the button to “Create Key”.
4. Name your key and assign access to a tool set.
5. Confirm and download your key in a ZIP file.

You will receive:

- a client-side SSL certificate signed by iAd
- a client-side SSL private key
- an access token

Use the client side SSL certificate, key, and access token when you call the `InitSession` method. This call authenticates, establishes a secure connection, and provides the session ID required to make further API calls.

As a security measure, three successive invalid authentication attempts will lock the API access for a minimum of four hours.

Implement your API-based app by following the API Method Reference in this document and use the following end point URL:

- The end point URL used for the Revenue API for News Publishers is `https://iadapi.apple.com/publisher/revenue/v1`.

This document describes the /v1 version of the iAd News Publishers API.

- The iAd News Publishers API supports JSON-RPC 2.0 payloads over HTTP POST. This allows you to create and update campaigns, lines, and ads programmatically.
- A request is a JSON-RPC 2.0 payload in an HTTP POST request with the `Content-Type` header of “application/json”.
- A response is a JSON-RPC 2.0 payload in an HTTP response request with the `Content-Type` header of “application/json” and is encoded as UTF-8.
- The request payload contains the method name and the method parameters, which in this API is a single Dictionary object.
- The response payload contains the result, which in this API will be a single Dictionary object.
- Any Array or List should contain uniform types. When an object contains sub-objects, it is referred to as a Collection. Within the JSON-RPC Dictionary objects, all keys must be String objects and the following primitives and objects may be represented (in nested forms): String, Number, Array, Dictionary, Boolean, NULL. For example, an Array may contain String objects, Number objects, other Array objects, or other Dictionary objects, which in turn may have other primitive types within them. Dictionary objects may have any primitive type for a given value, but the keys must be strings.

Versioning is managed through the URL. When new features are added to the iAd News Publishers API, as long as they are backward compatible, the URL will remain the same. If new features are added that are not backward compatible, a new URL will be introduced that supports those features and the unchanged features.

- There is no additional charge to use the Revenue API for News Publishers. However, there is a limit of 10,000 API calls per day (Midnight to Midnight, UTC), total for all iAd APIs. If you expect to make more API calls than this, contact the iAd team through the iAd Workbench “Contact Us” page.
- Because the communication protocol for the Revenue API for News Publishers is JSON RPC 2.0, any language that can perform HTTP `get` and `put` can be used to develop client programs.
- Request objects must follow the JSON-RPC 2.0 specification and must include the following fields:

  - __jsonrpc:__ A string specifying the version of JSON-RPC protocol. The string value must be exactly “2.0”.
  - __method:__ A string containing the name of the method to be invoked.
  - __id:__ A unique identifier established by your client program. It must be a string that ideally is unique for each call. The server will reply back using the same ID. If the input request `id` is unique, the output response will be uniquely assoctiated with the call that generated it. This field must be specified.
  - __params:__ An array of name-value pairs of named parameters and their corresponding values.
- Response objects follow the JSON-RPC 2.0 specification and include the following fields:

  - __jsonrpc:__ A String specifying the version of JSON-RPC protocol, which is exactly “2.0”.
  - __id:__ This will be provided in every response and is the same as the ID sent in the request object.
  - __result:__ In almost all cases, the result includes a `Success` attribute, a boolean value of `true` or `false` indicating success or failure of the API call. If `Success` is `true`, then `result` includes the response to the method request. If `Success` is `false`, then `result` includes an error message and an error code.

This section provides brief descriptions of the API interaction process and workflow phases, at a conceptual level.

Before you can interact with the iAd News Publishers API, you must provide your credentials and obtain a session ID. Your session ID is used in lieu of any other credentials, for the duration of your API interaction session.

The methods in the Revenue Reporting API for News Publishers allow you to download reporting data for the revenue produces by making your available ad placement inventory available for backfill.

- `GetChannelMetrics` — Obtain revenue performance metrics by channel.
- `GetChannelMetricsByCreativeType` — Obtain revenue performance metrics by creative (ad) type.

[Next](Summary%20of%20Revenue%20API%20for%20News%20Publishers%20Methods.md)

