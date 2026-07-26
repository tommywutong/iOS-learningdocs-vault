---
title: path
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/path
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/path'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/path.json'
content_hash: 'sha256:bb87fbde42e47b92'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# path

<sub>Instance Property</sub>

The path URL component, or nil if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var path: String? { get set }
```

## Discussion

For example, in the URL `http://www.example.com/index.html`, the path is `/index.html`.

## See Also

### Accessing components in native format

- [fragment](fragment.md) — The fragment URL component (the part after a `#` symbol), or nil if not present.
- [host](host.md) — The host URL subcomponent, or nil if not present.
- [encodedHost](encodedhost.md) — The host subcomponent, percent-encoded.
- [password](password.md) — The password URL subcomponent, or nil if not present.
- [port](port.md) — The port number URL component, or nil if not present.
- [query](query.md) — The query URL component as a string, or nil if not present.
- [queryItems](queryitems.md) — The query URL component as an array of name/value pairs.
- [scheme](scheme.md) — The scheme URL component, or nil if not present.
- [user](user.md) — The username URL subcomponent, or nil if not present.
