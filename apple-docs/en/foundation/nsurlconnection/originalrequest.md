---
title: originalRequest
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnection/originalrequest
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/originalrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/originalrequest.json'
content_hash: 'sha256:7149a633a59f7528'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# originalRequest

<sub>Instance Property</sub>

A deep copy of the original connection request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var originalRequest: URLRequest { get }
```

## Discussion

As the connection performs the load, the request may change as a result of protocol canonicalization or due to following redirects. [currentRequest](currentrequest.md) can be used to retrieve this value.

## See Also

### Connection URL Information

- [currentRequest](currentrequest.md) — The current connection request.
