---
title: query
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/query
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/query'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/query.json'
content_hash: 'sha256:c3d28322a38070a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# query

<sub>Instance Property</sub>

The query subcomponent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var query: String? { get set }
```

## Discussion

The getter for this property removes any percent encoding this component may have (if the component allows percent encoding). Setting this property assumes the subcomponent or component string is not percent encoded and will add percent encoding (if the component allows percent encoding).

## See Also

### Accessing components in native format

- [fragment](fragment.md) — The fragment subcomponent.
- [host](host.md) — The host subcomponent.
- [encodedHost](encodedhost.md) — The host subcomponent, percent-encoded.
- [password](password.md) — The password subcomponent of the URL.
- [path](path.md) — The path subcomponent.
- [port](port.md) — The port subcomponent.
- [queryItems](queryitems.md) — An array of query items for the URL in the order in which they appear in the original query string.
- [scheme](scheme.md) — The scheme subcomponent of the URL.
- [user](user.md) — The user subcomponent of the URL.
