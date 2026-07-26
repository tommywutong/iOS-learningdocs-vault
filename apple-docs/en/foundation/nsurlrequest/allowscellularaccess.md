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
doc_path: /documentation/foundation/nsurlrequest/allowscellularaccess
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/allowscellularaccess'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/allowscellularaccess.json'
content_hash: 'sha256:d4605112688ea126'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# allowsCellularAccess

<sub>Instance Property</sub>

A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowsCellularAccess: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the cellular radio can be used; [false](../../swift/false.md) otherwise.

## See Also

### Related Documentation

- [allowsCellularAccess](../nsmutableurlrequest/allowscellularaccess.md) — A Boolean value that indicates whether a connection can use the device’s cellular network (if present).

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldHandleCookies](httpshouldhandlecookies.md) — A Boolean value that indicates whether the default cookie handling will be used for this request.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
