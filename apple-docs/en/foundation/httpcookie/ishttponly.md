---
title: isHTTPOnly
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/ishttponly
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/ishttponly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/ishttponly.json'
content_hash: 'sha256:090575c52cafecad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# isHTTPOnly

<sub>Instance Property</sub>

A Boolean value that indicates whether the cookie should only be sent to HTTP servers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isHTTPOnly: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) if the cookie should only be sent using HTTP headers, [false](../../swift/false.md) otherwise.

Cookies can be marked as HTTP-only by a server (or by JavaScript code). Cookies marked as such must only be sent via HTTP Headers in HTTP requests for URLs that match both the path and domain of the respective cookies.

> [!note] Note
> [RFC 6265](https://tools.ietf.org/html/rfc6265) formally defines the `HttpOnly` attribute.

> [!important] Important
> To prevent cross-site scripting vulnerabilities, don’t deliver cookies marked as HTTP-only to JavaScript code.

## See Also

### Securing cookies

- [secure](issecure.md) — A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [sameSitePolicy](samesitepolicy.md) — A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [HTTPCookieStringPolicy](../httpcookiestringpolicy.md) — Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.
