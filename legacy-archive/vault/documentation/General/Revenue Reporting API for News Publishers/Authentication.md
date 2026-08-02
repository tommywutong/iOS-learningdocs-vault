---
title: Revenue Reporting API for News Publishers
apple_id: TP40016970
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2016-08-12'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iAd_News_Revenue_API/Document/Revenue_Ch3_Authentication.html
archived_at: '2026-07-15T07:34:29.601261Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Revenue Reporting API for News Publishers](Revenue%20API%20for%20News%20Publishers%20%E2%80%94%20Overview.md)


[Next](Revenue%20Methods.md)[Previous](Summary%20of%20Revenue%20API%20for%20News%20Publishers%20Methods.md)

# Authentication

The `InitSession` method authenticates your account, establishes a secure connection, and provides the session ID required to make other API calls. Call `InitSession` before doing anything else with the API.

The `InitSession` method requires your access token and returns a `SessionId` string. Use this `SessionId` string to authenticate all other API operations. A `SessionId` expires after one hour of inactivity.

| Parameter | Type | Required / Optional | Available | Comments |
| --- | --- | --- | --- | --- |
| `accessToken` | String | Required | /v1+ | `accessToken` is one of the keys given to a user along with client side certificate to initiate session. |

__Listing 3-1__  InitSession Sample Input

```json
{
   "method":"InitSession",
   "id":"1000",
   "params":{
      "accessToken":"1234567890"
   },
   "jsonrpc":"2.0"
}
```


| Parameter | Type | Available | Comments |
| --- | --- | --- | --- |
| `SessionId` | String | /v1+ | `SessionId` that needs to be used for all other API operations. |

__Listing 3-2__  InitSession Sample Output

```json
{ "id": "RequestNo-001",
  "result": {
    "SessionId": "44e5b59211ae0da9c9739b0866936ca94301d444"
  },
  "jsonrpc": "2.0"
}
```

[Next](Revenue%20Methods.md)[Previous](Summary%20of%20Revenue%20API%20for%20News%20Publishers%20Methods.md)

