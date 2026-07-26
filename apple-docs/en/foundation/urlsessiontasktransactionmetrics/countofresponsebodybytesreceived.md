---
title: countOfResponseBodyBytesReceived
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesreceived
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesreceived'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesreceived.json'
content_hash: 'sha256:3a8b41b78e9577b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# countOfResponseBodyBytesReceived

<sub>Instance Property</sub>

The number of bytes transferred for the response body.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfResponseBodyBytesReceived: Int64 { get }
```

## Discussion

This value includes protocol-specific framing, transfer encoding, and content encoding.

## See Also

### Accessing data transfer metrics

- [countOfRequestBodyBytesBeforeEncoding](countofrequestbodybytesbeforeencoding.md) — The size of the upload body data, file, or stream, in bytes.
- [countOfRequestBodyBytesSent](countofrequestbodybytessent.md) — The number of bytes transferred for the request body.
- [countOfRequestHeaderBytesSent](countofrequestheaderbytessent.md) — The number of bytes transferred for the request header.
- [countOfResponseBodyBytesAfterDecoding](countofresponsebodybytesafterdecoding.md) — The size of data delivered to your delegate or completion handler.
- [countOfResponseHeaderBytesReceived](countofresponseheaderbytesreceived.md) — The number of bytes transferred for the response header.
