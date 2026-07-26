---
title: httpShouldHandleCookies
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmutableurlrequest/httpshouldhandlecookies
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableurlrequest/httpshouldhandlecookies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableurlrequest/httpshouldhandlecookies.json'
content_hash: 'sha256:e16b294d2d4fe6d4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableURLRequest](../nsmutableurlrequest.md)

# httpShouldHandleCookies

<sub>Instance Property</sub>

A Boolean value that indicates whether the request should use the default cookie handling for the request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldHandleCookies: Bool { get set }
```

## Discussion

[true](../../swift/true.md) if the request should use the default cookie handling for the request, [false](../../swift/false.md) otherwise. The default is [true](../../swift/true.md).

If your app sets the `Cookie` header on an [NSMutableURLRequest](../nsmutableurlrequest.md) object, then this method has no effect, and the cookie data you set in the header overrides all cookies from the cookie store.

### Special considerations

In OS X v10.2 with Safari 1.0 the value set by this method is not respected by the framework.

## See Also

### Related Documentation

- [HTTPShouldHandleCookies](../nsurlrequest/httpshouldhandlecookies.md) — A Boolean value that indicates whether the default cookie handling will be used for this request.

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request can continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether a connection can use the device’s cellular network (if present).
