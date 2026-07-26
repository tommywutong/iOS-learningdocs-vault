---
title: encodedHost
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/encodedhost
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/encodedhost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/encodedhost.json'
content_hash: 'sha256:68c1a01f09ce23a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# encodedHost

<sub>Instance Property</sub>

The host subcomponent, percent-encoded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var encodedHost: String? { get set }
```

## Discussion

The getter for this property retains any percent-encoding this component may have. Setting this property assumes the component string already has the correct percent-encoding. Attempting to set an incorrectly percent-encoded string raises [fatalError(_:file:line:)](<../../swift/fatalerror(__file_line_).md>).

## See Also

### Accessing components in native format

- [fragment](fragment.md) — The fragment subcomponent.
- [host](host.md) — The host subcomponent.
- [password](password.md) — The password subcomponent of the URL.
- [path](path.md) — The path subcomponent.
- [port](port.md) — The port subcomponent.
- [query](query.md) — The query subcomponent.
- [queryItems](queryitems.md) — An array of query items for the URL in the order in which they appear in the original query string.
- [scheme](scheme.md) — The scheme subcomponent of the URL.
- [user](user.md) — The user subcomponent of the URL.
