---
title: sameSitePolicy
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/samesitepolicy
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/samesitepolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/samesitepolicy.json'
content_hash: 'sha256:94565559dd8c8a51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# sameSitePolicy

<sub>Instance Property</sub>

A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sameSitePolicy: HTTPCookieStringPolicy? { get }
```

## Discussion

Along with the policy values defined by [HTTPCookieStringPolicy](../httpcookiestringpolicy.md), this property may also be `nil`. In this case, cross-site requests include the cookie.

## See Also

### Securing cookies

- [HTTPOnly](ishttponly.md) — A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [secure](issecure.md) — A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [HTTPCookieStringPolicy](../httpcookiestringpolicy.md) — Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.
