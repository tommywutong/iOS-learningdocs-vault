---
title: password
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/password
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/password'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/password.json'
content_hash: 'sha256:1a7aa0c4295cde49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# password

<sub>Instance Property</sub>

The password URL subcomponent, or nil if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var password: String? { get set }
```

## Discussion

For example, in the URL `http://username:password@www.example.com/index.html`, the password is `password`.

## See Also

### Accessing components in native format

- [fragment](fragment.md) — The fragment URL component (the part after a `#` symbol), or nil if not present.
- [host](host.md) — The host URL subcomponent, or nil if not present.
- [encodedHost](encodedhost.md) — The host subcomponent, percent-encoded.
- [path](path.md) — The path URL component, or nil if not present.
- [port](port.md) — The port number URL component, or nil if not present.
- [query](query.md) — The query URL component as a string, or nil if not present.
- [queryItems](queryitems.md) — The query URL component as an array of name/value pairs.
- [scheme](scheme.md) — The scheme URL component, or nil if not present.
- [user](user.md) — The username URL subcomponent, or nil if not present.
