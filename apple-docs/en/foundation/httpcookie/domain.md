---
title: domain
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.2+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/httpcookie/domain
source_url: 'https://developer.apple.com/documentation/foundation/httpcookie/domain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/httpcookie/domain.json'
content_hash: 'sha256:a497683d1b0e04fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [HTTPCookie](../httpcookie.md)

# domain

<sub>Instance Property</sub>

The domain of the cookie.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var domain: String { get }
```

## Discussion

If the domain does not start with a dot, then the cookie is only sent to the exact host specified by the domain. If the domain does start with a dot, then the cookie is sent to other hosts in that domain as well, subject to certain restrictions. See [RFC 6265](https://tools.ietf.org/html/rfc6265.html) for more detail.

## See Also

### Getting cookie host properties

- [path](path.md) — The cookie’s path.
- [portList](portlist.md) — The cookie’s port list.
