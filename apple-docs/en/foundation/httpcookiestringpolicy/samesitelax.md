---
title: sameSiteLax
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookiestringpolicy/samesitelax
source_url: 'https://developer.apple.com/documentation/foundation/httpcookiestringpolicy/samesitelax'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookiestringpolicy/samesitelax.json'
content_hash: 'sha256:31d48299ff83ead6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookieStringPolicy](../httpcookiestringpolicy.md)

# sameSiteLax

<sub>Type Property</sub>

A policy that allows certain cross-site requests to include the cookie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let sameSiteLax: HTTPCookieStringPolicy
```

## Discussion

When a cookie has this policy, a request includes the cookie if the request is “top-level,”, meaning one that changes the URL in the address bar.

## See Also

### Policies

- [NSHTTPCookieSameSiteStrict](samesitestrict.md) — A policy that prohibits a cross-site request from including the cookie.
