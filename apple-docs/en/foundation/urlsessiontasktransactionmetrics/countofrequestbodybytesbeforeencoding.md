---
title: countOfRequestBodyBytesBeforeEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlsessiontasktransactionmetrics/countofrequestbodybytesbeforeencoding
source_url: 'https://developer.apple.com/documentation/foundation/urlsessiontasktransactionmetrics/countofrequestbodybytesbeforeencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlsessiontasktransactionmetrics/countofrequestbodybytesbeforeencoding.json'
content_hash: 'sha256:56dbc8660829b097'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLSessionTaskTransactionMetrics](../urlsessiontasktransactionmetrics.md)

# countOfRequestBodyBytesBeforeEncoding

<sub>Instance Property</sub>

The size of the upload body data, file, or stream, in bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var countOfRequestBodyBytesBeforeEncoding: Int64 { get }
```

## See Also

### Accessing data transfer metrics

- [countOfRequestBodyBytesSent](countofrequestbodybytessent.md) — The number of bytes transferred for the request body.
- [countOfRequestHeaderBytesSent](countofrequestheaderbytessent.md) — The number of bytes transferred for the request header.
- [countOfResponseBodyBytesAfterDecoding](countofresponsebodybytesafterdecoding.md) — The size of data delivered to your delegate or completion handler.
- [countOfResponseBodyBytesReceived](countofresponsebodybytesreceived.md) — The number of bytes transferred for the response body.
- [countOfResponseHeaderBytesReceived](countofresponseheaderbytesreceived.md) — The number of bytes transferred for the response header.
