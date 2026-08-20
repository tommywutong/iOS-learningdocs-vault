---
title: PassKit Web Service Reference
apple_id: TP40011988
resource_type: Guide
platform: iOS
topic: User Experience
technology: PassKit
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/documentation/PassKit/Reference/PassKit_WebService/WebService.html
archived_at: '2026-07-27T06:57:08.719393Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Document%20Revision%20History.md)

# PassKit Web Service Reference

__Companion Guide:__ _[Wallet Developer Guide](../../User%20Experience/Wallet%20Developer%20Guide/index.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdcojv)_

A Representational State Transfer (REST)–style web service protocol is used to communicate with your server about changes to passes, and to fetch the latest version of a pass when it has changed. The endpoints always begin with the web service URL, as specified in the pass, followed by the protocol version number. For example, a request for the latest version of the pass of type `com.apple.pass.example` and serial number `ABC123` might look like the following:

（原归档配图获取待重试：`web_service_url_2x.png`）

All of the endpoints, including the logging endpoint, are required.

For all endpoints, specify the `application/json` MIME type for responses that contain JSON data, and the `application/vnd.apple.pkpass` for responses that contain a Wallet pass.

If a request fails—for example, due to a network connectivity issue—PassKit tries again several times after waiting a period of time. Each time it tries again, it waits longer. If the request continues to fail, it eventually gives up.

## Registering a Device to Receive Push Notifications for a Pass

POST request to _webServiceURL_`/`_version_`/devices/`_deviceLibraryIdentifier_`/registrations/`_passTypeIdentifier_`/`_serialNumber_

__Parameters__

**_webServiceURL_**
: The URL to your web service, as specified in the pass.

**_version_**
: The protocol version—currently, v1.

**_deviceLibraryIdentifier_**
: A unique identifier that is used to identify and authenticate this device in future requests.

**_passTypeIdentifier_**
: The pass’s type, as specified in the pass.

**_serialNumber_**
: The pass’s serial number, as specified in the pass.

__Header__

The Authorization header is supplied; its value is the word `ApplePass`, followed by a space, followed by the pass’s authorization token as specified in the pass.

__Payload__

The POST payload is a JSON dictionary containing a single key and value:

**_pushToken_**
: The push token that the server can use to send push notifications to this device.

__Response__

- If the serial number is already registered for this device, returns HTTP status 200.
- If registration succeeds, returns HTTP status 201.
- If the request is not authorized, returns HTTP status 401.
- Otherwise, returns the appropriate standard HTTP status.

__Discussion__

Any time the pass is updated, your server sends a push notification with an empty JSON dictionary as the payload to the device using the given push notification token. This process continues until the device is explicitly unregistered (as described in [Unregistering a Device](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytsobyfvbuqmbnknltk)).

## Getting the Serial Numbers for Passes Associated with a Device

GET request to _webServiceURL_`/`_version_`/devices/`_deviceLibraryIdentifier_`/registrations/`_passTypeIdentifier_`?passesUpdatedSince=`_tag_

__Parameters__

**_webServiceURL_**
: The URL to your web service, as specified in the pass.

**_version_**
: The protocol version—currently, v1.

**_deviceLibraryIdentifier_**
: A unique identifier that is used to identify and authenticate the device.

**_passTypeIdentifier_**
: The pass’s type, as specified in the pass.

**_tag_**
: A tag from a previous request. _(optional)_

If the `passesUpdatedSince` parameter is present, returns only the passes that have been updated since the time indicated by `tag`. Otherwise, returns all passes.

__Response__

- If there are matching passes, returns HTTP status 200 with a JSON dictionary with the following keys and values:

  **`lastUpdated` (string)**
  : The current modification tag.

  **`serialNumbers` (array of strings)**
  : The serial numbers of the matching passes.
- If there are no matching passes, returns HTTP status 204.
- Otherwise, returns the appropriate standard HTTP status.

__Discussion__

The modification tag is used to give a name to a point in time. It is typically convenient to use a timestamp, but the server can use another approach. The tag is treated as an opaque value by the system.

## Getting the Latest Version of a Pass

GET request to _webServiceURL_`/`_version_`/passes/`_passTypeIdentifier_`/`_serialNumber_

__Parameters__

**_webServiceURL_**
: The URL to your web service, as specified in the pass.

**_version_**
: The protocol version—currently, v1.

**_passTypeIdentifier_**
: The pass’s type, as specified in the pass.

**_serialNumber_**
: The unique pass identifier, as specified in the pass.

__Header__

The Authorization header is supplied; its value is the word `ApplePass`, followed by a space, followed by the pass’s authorization token as specified in the pass.

__Response__

- If request is authorized, returns HTTP status 200 with a payload of the pass data.
- If the request is not authorized, returns HTTP status 401.
- Otherwise, returns the appropriate standard HTTP status.

__Discussion__

Support standard HTTP caching on this endpoint: Check for the `If-Modified-Since` header, and return HTTP status code 304 if the pass has not changed.

## Unregistering a Device

DELETE request to _webServiceURL_`/`_version_`/devices/`_deviceLibraryIdentifier_`/registrations/`_passTypeIdentifier_/_serialNumber_

__Parameters__

**_webServiceURL_**
: The URL to your web service, as specified in the pass.

**_version_**
: The protocol version—currently, v1.

**_deviceLibraryIdentifier_**
: A unique identifier that is used to identify and authenticate the device.

**_passTypeIdentifier_**
: The pass’s type, as specified in the pass.

**_serialNumber_**
: The unique pass identifier, as specified in the pass.

__Header__

The Authorization header is supplied; its value is the word `ApplePass`, followed by a space, followed by the pass’s authorization token as specified in the pass.

__Response__

- If disassociation succeeds, returns HTTP status 200.
- If the request is not authorized, returns HTTP status 401.
- Otherwise, returns the appropriate standard HTTP status.

__Discussion__

The server disassociates the specified device from the pass, and no longer sends push notifications to this device when the pass changes.

## Logging Errors

POST request to _webServiceURL_`/`_version_`/log`

__Parameters__

**_webServiceURL_**
: The URL to your web service, as specified in the pass.

**_version_**
: The protocol version—currently, v1.

__Payload__

The POST payload is a JSON dictionary, containing a single key and value:

**`logs` (string)**
: An array of log messages as strings.

__Response__

Returns HTTP status 200.

__Discussion__

This endpoint is intended to help you debug your web service implementation. Log messages contain a description of the error in a human-readable format.

[Next](Document%20Revision%20History.md)
