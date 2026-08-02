---
title: Xcode Server API Reference
apple_id: TP40016472
resource_type: Guide
platform: Xcode Developer Tools
topic: Xcode
technology: null
published: '2016-03-21'
source_url: https://developer.apple.com/library/archive/documentation/Xcode/Conceptual/XcodeServerAPIReference/index.html
archived_at: '2026-07-18T02:24:25.633190Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)



## Overview

The Xcode Server API Reference is the underlying interface for Xcode Server.

> [!NOTE]
> 

### HTTPS Only

Use HTTPS to make all Xcode Server requests.

### UTF-8 Encoding

Every string passed to and from the Xcode Server API needs to be UTF-8 encoded.

### Error Handling

Errors are returned using standard HTTP error code syntax. Any additional info is included in the body of the response, JSON-formatted:

1. `{`
2. `"status": 401,`
3. `"message": "Unauthorized: invalid credentials"`
4. `}`

List of supported error codes:

1. `400: Bad Request`
2. `401: Unauthorized`
3. `403: Forbidden`
4. `404: Not Found`
5. `409: Conflict`
6. `410: Gone`
7. `500: Internal Server Error`
8. `501: Not Implemented`
9. `502: Bad Gateway`
10. `503: Service Unavailable`
11. `523: Service is not Enabled`
12. `530: Client unsupported.`
13. `531: ACL expansion not yet completed.`
14. `532: Service maintenance task active`

### Versioning

The version is set in the header using `X-XCSAPIVersion`. If you omit this property, Xcode Server assumes the latest version.

### Request Headers

All Xcode Server responses contain the version number of the API that the server supports. The version number is set in the response header using `X-XCSAPIVersion`.

### Schema

The section contains detailed information about the contents and meaning of the various payload structures used in Xcode Server requests and responses.

### Document ID and Revision

Xcode Server stores the data in documents. Each document in CouchDB has at least two properties: `_id` and `_rev`.

- `_id` is a unique identifier that makes the document unique.
- `_rev` is a value that changes every time the document is modified.

[Bots](Bots.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqge3dinzsfvbuqmrnknltc)
