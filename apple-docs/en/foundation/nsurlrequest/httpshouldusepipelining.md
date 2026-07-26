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
doc_path: /documentation/foundation/nsurlrequest/httpshouldusepipelining
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/httpshouldusepipelining'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/httpshouldusepipelining.json'
content_hash: 'sha256:0ba7a3eef50f59b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# httpShouldUsePipelining

<sub>Instance Property</sub>

A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission.

> [!warning] Deprecated
> Only supported in the classic loader, please adopt HTTP/2 and HTTP/3 instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldUsePipelining: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the request should continue transmitting data; otherwise, [false](../../swift/false.md).

## See Also

### Related Documentation

- [HTTPShouldUsePipelining](../nsmutableurlrequest/httpshouldusepipelining.md) — A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the default cookie handling will be used for this request.
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).
