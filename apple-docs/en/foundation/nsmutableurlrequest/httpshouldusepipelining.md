---
title: httpShouldUsePipelining
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（18.4 起废弃）, iPadOS 4.0+（18.4 起废弃）, Mac Catalyst 13.1+（18.4 起废弃）, macOS 10.7+（15.4 起废弃）, tvOS 9.0+（18.4 起废弃）, visionOS 1.0+（2.4 起废弃）, watchOS 2.0+（11.4 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsmutableurlrequest/httpshouldusepipelining
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldusepipelining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/httpshouldusepipelining.json'
content_hash: 'sha256:77f2f7c2956363ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# httpShouldUsePipelining

<sub>Instance Property</sub>

A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission.

> [!warning] Deprecated
> Only supported in the classic loader, please adopt HTTP/2 and HTTP/3 instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldUsePipelining: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the request should continue transmitting data, [false](../../swift/false.md) if the request should wait for a response. The default value is [false](../../swift/false.md).

Setting this property to [true](../../swift/true.md) value does not guarantee HTTP pipelining behavior. This may have no effect if an HTTP proxy is configured, or if the HTTP request uses an unsafe request method—for example, POST requests will not pipeline. Pipelining behavior may not begin until the second request on a given TCP connection. There may be other situations where pipelining does not occur even though this property is set to [true](../../swift/true.md). HTTP 1.1 allows the client to send multiple requests to the server without waiting for a response. Though HTTP 1.1 requires support for pipelining, some servers report themselves as being HTTP 1.1 but do not support pipelining (disconnecting, sending resources in the wrong order, omitting part of a resource, etc.).

## See Also

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the request should use the default cookie handling for the request.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
