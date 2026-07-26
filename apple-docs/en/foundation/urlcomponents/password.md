---
title: password
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/password
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/password'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/password.json'
content_hash: 'sha256:a68516064c21ba32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# password

<sub>Instance Property</sub>

The password subcomponent of the URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var password: String? { get set }
```

## Discussion

The getter for this property removes any percent encoding this component may have (if the component allows percent encoding). Setting this property assumes the subcomponent or component string is not percent encoded and will add percent encoding (if the component allows percent encoding).

Warning: IETF STD 66 (rfc3986) says the use of the format “user:password” in the userinfo subcomponent of a URI is deprecated because passing authentication information in clear text has proven to be a security risk. However, there are cases where this practice is still needed, and so the user and password components and methods are provided.

## See Also

### Accessing components in native format

- [fragment](fragment.md) — The fragment subcomponent.
- [host](host.md) — The host subcomponent.
- [encodedHost](encodedhost.md) — The host subcomponent, percent-encoded.
- [path](path.md) — The path subcomponent.
- [port](port.md) — The port subcomponent.
- [query](query.md) — The query subcomponent.
- [queryItems](queryitems.md) — An array of query items for the URL in the order in which they appear in the original query string.
- [scheme](scheme.md) — The scheme subcomponent of the URL.
- [user](user.md) — The user subcomponent of the URL.
