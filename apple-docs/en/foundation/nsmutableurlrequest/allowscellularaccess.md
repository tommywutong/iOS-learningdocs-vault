---
title: allowsCellularAccess
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest/allowscellularaccess
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/allowscellularaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/allowscellularaccess.json'
content_hash: 'sha256:16e58ca7edb9cfdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# allowsCellularAccess

<sub>Instance Property</sub>

A Boolean value that indicates whether a connection can use the device’s cellular network (if present).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCellularAccess: Bool { get set }
```

## Discussion

Setting this property to [true](../../swift/true.md) (the default) makes the request eligible to run over cellular, subject to other considerations (including, but not limited to, the [allowsCellularAccess](../urlsessionconfiguration/allowscellularaccess.md) property of the [URLSessionConfiguration](../urlsessionconfiguration.md)). Setting this value to [false](../../swift/false.md) ensures that the request will never run over cellular.

## See Also

### Related Documentation

- [waitsForConnectivity](../urlsessionconfiguration/waitsforconnectivity.md) — A Boolean value that indicates whether the session should wait for connectivity to become available, or fail immediately.

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
