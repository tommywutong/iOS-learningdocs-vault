---
title: Campaign Management API for News Publishers
apple_id: TP40016670
resource_type: Guide
platform: iAd System JS|iAd Producer|iOS
topic: General
technology: null
published: '2018-05-10'
source_url: https://developer.apple.com/library/archive/documentation/General/Conceptual/iAd_News_Campaign_API/Book/Overview.html
archived_at: '2026-07-27T06:57:10.277221Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



# Campaign Management API for News Publishers — Overview

Apple News publishers have the ability to launch, monitor, and report on _direct-sold_ and _house_ advertising campaigns via “[Workbench for News Publishers](https://iadworkbench.apple.com/)”.

The Campaign Management API for News Publishers described in this document provides programmatic access to Apple’s campaign management API server, where you can use your own tools and programs to do the same kinds of tasks as you would do with the Workbench:

- Manage ad campaigns on Apple News.
- Retrieve performance metrics for ad campaigns.
- Estimate the availability of inventory for ad placements in Apple News.

## Access, Authentication, and Authorization

The Campaign Management API for News Publishers is available to all Apple News publisher accounts that have access to News Publisher tools on [Workbench](https://iadworkbench.apple.com).

Client side SSL certificate is used to authenticate the user. An access token provides authorization to all of the API.

To access the Advertising Platforms API server, you can request and download the required API keys, tokens, and certificates from the [Workbench](https://iadworkbench.apple.com) site.

1. Click on the dropdown arrow next to your account name near the top right and choosing Account from the dropdown menu.
2. Select the API tab under the page title.
3. Click the button to “Create Key”.
4. Name your key and assign access to a tool set.
5. Enter the “Captcha” text.
6. Confirm and download your key in a ZIP file.

You will receive:

- `certificate.pem` — a client-side SSL certificate signed by Apple Ad Platforms. This is
- `private_key.key` — a client-side SSL private key
- `token.txt` — an access token

The certificate that you download is a PEM file, which is typically used with Python. The following commands use the publically available `openssl` and `keytool` utilities to convert the PEM certificate to P12 or JKS formats as needed. Use the first command to convert your PEM-format certificate to a P12-format certificate, typically used with RESTful systems. Use the second to convert that P12-format certificate to a JKS-format certificate, typically used with Java.

```
openssl pkcs12 -export -in certificate.pem -inkey private_key.key -out certificate.p12 -name “<NAME>"
keytool -v -importkeystore -srckeystore certificate.p12 -srcstoretype PKCS12 -destkeystore certificate.jks -deststoretype JKS
```

Use your client-side SSL certificate, key, and access token when you call the `InitSession` method. This call authenticates, establishes a secure connection, and provides the session ID required to make further API calls.

As a security measure, ten successive invalid authentication attempts will lock the API access for a minimum of five hours.

## API Endpoint

Implement your API-based app by following the API Method Reference in this document and use the following end point URL:

- The end point URL used for the Campaign Management API for News Publishers is `https://iadapi.apple.com/publisher/campaigns/v1`

__Note:__
Communication with the web service must be over https.

This document describes the /v1 version of the Apple Advertising Platforms News Publishers API.

## API Basics

- The News Publishers API supports JSON-RPC 2.0 payloads over HTTP POST. This allows you to create and update campaigns, lines, and ads programmatically.
- A request is a JSON-RPC 2.0 payload in an HTTP POST request with the `Content-Type` header of “application/json”.
- A response is a JSON-RPC 2.0 payload in an HTTP response with the `Content-Type` header of “application/json” and is encoded as UTF-8.
- The request payload contains the method name and the method parameters, which in this API is a single Dictionary object.
- The response payload contains the result, which in this API will be a single Dictionary object.

## Versioning of the API

Versioning is managed through the URL. When new features are added to the News Publishers API, as long as they are backward compatible, the URL will remain the same. If new features are added that are not backward compatible, a new URL will be introduced that supports those features and the unchanged features.

## Invoking the API

- There is no additional charge to use the Campaign Management API for News Publishers. However, there is a limit of 10,000 API calls per day (Midnight to Midnight, UTC), total for all Advertising Platforms APIs. If you expect to make more API calls than this, contact the Advertising Platforms team through the Workbench “Contact Us” page.
- Because the communication protocol for the Campaign Management API for News Publishers is JSON RPC 2.0, any language that can perform HTTP POST can be used to develop client programs.
- Request objects must follow the JSON-RPC 2.0 specification and must include the following fields:

  - __jsonrpc:__ A string specifying the version of JSON-RPC protocol. The string value must be exactly “2.0”.
  - __method:__ A string containing the name of the method to be invoked.
  - __id:__ A unique identifier established by your client program. It must be a string that ideally is unique for each call. The server will reply back using the same ID. If the input request `id` is unique, the output response will be uniquely assoctiated with the call that generated it. This field must be specified.
  - __params:__ An array of name-value pairs of named parameters and their corresponding values.
- Response objects follow the JSON-RPC 2.0 specification and include the following fields:

  - __jsonrpc:__ A String specifying the version of JSON-RPC protocol, which is exactly “2.0”.
  - __id:__ This will be provided in every response and is the same as the ID sent in the request object.
  - __result:__ In almost all cases, the result includes a `Success` attribute, a boolean value of `true` or `false` indicating success or failure of the API call. If `Success` is `true`, then `result` includes the response to the method request. If `Success` is `false`, then `result` includes an error message and an error code.

    __Note:__
    The `InitSession` methos do not return a `Success` attribute and `UploadAsset` returns a string for `Success` rather than a Boolean.

## API Concepts

This section provides brief descriptions of the API interaction process and workflow phases, at a conceptual level.

### Authentication

Before you can interact with the News Publishers API, you must provide your credentials, access token, and certificate, and obtain a session ID. Your session ID is used for the duration of your API interaction session.

### Helper Methods for Campaign Creation Workflow

These methods provide data that is not specific to individual campaigns. This data includes campaign categories, available ad types, ads you have created in Producer, targeting parameters, and time zones.

### Campaign and Line Creation

These methods allow you to create campaigns and lines, using the information provided by helper methods, as appropriate, upload ads, associate ads to specific lines, and submit your campaign.

### Managing Campaign Methods

This section includes methods that allow you to update campaigns and lines and to activate and pause campaigns, lines, and ads.

### Inventory Methods

Ad placement inventory consists of the ad locations that are available for sale. For privacy and security, these are aggregated and tracked statistically. The methods in this section allow you to check, reserve, and unreserve available inventory.

### Reporting Methods

You can use the API to download reporting data for your campaigns lines, and ads that were created using the Workbench UI.

- To get campaign summary or details, use the methods `GetCampaignSummary` or `GetCampaignDetails`.
- To get line or ad details, use the methods`GetLineDetails` or `GetAdDetails`.
- To get the metrics, use the following methods based on the level at which you need the data:

  - `GetCampaignMetrics`
  - `GetLineMetrics`
  - `GetAdMetrics`
