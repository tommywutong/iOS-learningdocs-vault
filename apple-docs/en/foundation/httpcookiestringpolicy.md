---
title: HTTPCookieStringPolicy
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiestringpolicy
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestringpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestringpolicy.json'
content_hash: 'sha256:f72a68dce4067ca6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# HTTPCookieStringPolicy

<sub>Structure</sub>

Values that indicate whether to restrict the cookie to requests sent back to the same site that created it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HTTPCookieStringPolicy
```

## Discussion

[RFC 6265](https://tools.ietf.org/html/draft-ietf-httpbis-cookie-same-site-00) defines “same site” as the registerable domain of a URI.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a policy

- [init(rawValue:)](<httpcookiestringpolicy/init(rawvalue_).md>) — Creates an HTTP cookie string policy from the given raw string.

### Policies

- [NSHTTPCookieSameSiteStrict](httpcookiestringpolicy/samesitestrict.md) — A policy that prohibits a cross-site request from including the cookie.
- [NSHTTPCookieSameSiteLax](httpcookiestringpolicy/samesitelax.md) — A policy that allows certain cross-site requests to include the cookie.

## See Also

### Securing cookies

- [HTTPOnly](httpcookie/ishttponly.md) — A Boolean value that indicates whether the cookie should only be sent to HTTP servers.
- [secure](httpcookie/issecure.md) — A Boolean value that indicates whether the cookie may only be sent over secure channels.
- [sameSitePolicy](httpcookie/samesitepolicy.md) — A Boolean value that indicates whether to restrict the cookie to requests sent back to the same site that created it.
