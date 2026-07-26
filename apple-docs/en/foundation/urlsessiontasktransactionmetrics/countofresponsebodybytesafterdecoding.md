---
title: countOfResponseBodyBytesAfterDecoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/countofresponsebodybytesafterdecoding.json'
content_hash: 'sha256:c716849af67a6e7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# countOfResponseBodyBytesAfterDecoding

<sub>Instance Property</sub>

The size of data delivered to your delegate or completion handler.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfResponseBodyBytesAfterDecoding: Int64 { get }
```

## See Also

### Accessing data transfer metrics

- [countOfRequestBodyBytesBeforeEncoding](countofrequestbodybytesbeforeencoding.md) — The size of the upload body data, file, or stream, in bytes.
- [countOfRequestBodyBytesSent](countofrequestbodybytessent.md) — The number of bytes transferred for the request body.
- [countOfRequestHeaderBytesSent](countofrequestheaderbytessent.md) — The number of bytes transferred for the request header.
- [countOfResponseBodyBytesReceived](countofresponsebodybytesreceived.md) — The number of bytes transferred for the response body.
- [countOfResponseHeaderBytesReceived](countofresponseheaderbytesreceived.md) — The number of bytes transferred for the response header.
