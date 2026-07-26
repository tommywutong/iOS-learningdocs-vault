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
doc_path: /documentation/foundation/nsurlrequest/httpshouldhandlecookies
source_url: 'https://developer.apple.com/documentation/foundation/nsurlrequest/httpshouldhandlecookies'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlrequest/httpshouldhandlecookies.json'
content_hash: 'sha256:b4698a74640b311b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLRequest](../nsurlrequest.md)

# httpShouldHandleCookies

<sub>Instance Property</sub>

A Boolean value that indicates whether the default cookie handling will be used for this request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var httpShouldHandleCookies: Bool { get }
```

## Discussion

[true](../../swift/true.md) if the default cookie handling will be used for this request, [false](../../swift/false.md) otherwise. The default is [true](../../swift/true.md).

## See Also

### Related Documentation

- [HTTPShouldHandleCookies](../nsmutableurlrequest/httpshouldhandlecookies.md) — A Boolean value that indicates whether the request should use the default cookie handling for the request.

### Controlling request behavior

- [timeoutInterval](timeoutinterval.md) — The request’s timeout interval, in seconds.
- [HTTPShouldUsePipelining](httpshouldusepipelining.md) — A Boolean value that indicates whether the request should continue transmitting data before receiving a response from an earlier transmission. _(deprecated)_
- [allowsCellularAccess](allowscellularaccess.md) — A Boolean value that indicates whether the request is allowed to use the cellular radio (if present).
