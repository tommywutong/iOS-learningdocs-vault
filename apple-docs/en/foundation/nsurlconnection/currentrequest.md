---
title: currentRequest
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlconnection/currentrequest
source_url: 'https://developer.apple.com/documentation/foundation/nsurlconnection/currentrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlconnection/currentrequest.json'
content_hash: 'sha256:fc11f8fd43d2f714'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLConnection](../nsurlconnection.md)

# currentRequest

<sub>Instance Property</sub>

The current connection request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentRequest: URLRequest { get }
```

## Discussion

As the connection performs the load, the request may change as a result of protocol canonicalization or due to following redirects. This property provides the current value of the request.

## See Also

### Connection URL Information

- [originalRequest](originalrequest.md) — A deep copy of the original connection request.
