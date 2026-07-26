---
title: 'connection(_:needNewBodyStream:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsurlconnectiondatadelegate/connection(_:neednewbodystream:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnectiondatadelegate/connection(_:neednewbodystream:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnectiondatadelegate/connection%28_%3Aneednewbodystream%3A%29.json'
content_hash: 'sha256:1bb5e4829ba5112c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnectionDataDelegate](../nsurlconnectiondatadelegate.md)

# connection(_:needNewBodyStream:)

<sub>Instance Method</sub>

Called when an `NSURLConnection` needs to retransmit a request that has a body stream to provide a new, unopened stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func connection(_ connection: NSURLConnection, needNewBodyStream request: URLRequest) -> InputStream?
```

## Parameters

- `connection` — The NSURLConnection that is requesting a new body stream.

## Return Value

This delegate method should return a new, unopened stream that provides the body contents for the request.

If this delegate method returns `NULL`, the connection fails.

## Discussion

In macOS, if this method is not implemented, body stream data is spooled to disk in case retransmission is required. This spooling may not be desirable for large data sets.

By implementing this delegate method, the client opts out of automatic spooling, and must provide a new, unopened stream for each retransmission.

## See Also

### Handling Redirects

- [- connection:willSendRequest:redirectResponse:](<connection(__willsend_redirectresponse_).md>) — Sent when the connection determines that it must change URLs in order to continue loading a request.
