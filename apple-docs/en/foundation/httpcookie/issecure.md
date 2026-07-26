---
title: isSecure
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/issecure
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/issecure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/issecure.json'
content_hash: 'sha256:95c8a8618de58113'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# isSecure

<sub>Instance Property</sub>

A Boolean value that indicates whether the cookie may only be sent over secure channels.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSecure: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) if this cookie should only be sent over secure channels, otherwise [false](../../swift/false.md).

## See Also

### Securing cookies

- [HTTPOnly](ishttponly.md) — A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [sameSitePolicy](samesitepolicy.md) — A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
- [HTTPCookieStringPolicy](../httpcookiestringpolicy.md) — Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.
