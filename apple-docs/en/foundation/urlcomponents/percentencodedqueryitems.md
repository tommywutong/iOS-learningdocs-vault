---
title: percentEncodedQueryItems
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 11.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/percentencodedqueryitems
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/percentencodedqueryitems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/percentencodedqueryitems.json'
content_hash: 'sha256:8431a253273e8dd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# percentEncodedQueryItems

<sub>Instance Property</sub>

The query subcomponent, as an array of percent-encoded query items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedQueryItems: [URLQueryItem]? { get set }
```

## Discussion

The setter combines an array containing any number of [URLQueryItem](../urlqueryitem.md) key-value pairs into a query string and sets the `URLComponents` query property. This property assumes the query item names and values are already correctly percent-encoded. It also assumes that the query item names don’t contain the query item delimiter characters `&` and `=`. Attempting to set an incorrectly percent-encoded query item or a query item name with the query item delimiter characters `&` and `=` raises [fatalError(_:file:line:)](<../../swift/fatalerror(__file_line_).md>).

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment subcomponent, percent-encoded.
- [percentEncodedHost](percentencodedhost.md) — The host subcomponent, percent-encoded. _(deprecated)_
- [percentEncodedPassword](percentencodedpassword.md) — The password subcomponent, percent-encoded.
- [percentEncodedPath](percentencodedpath.md) — The path subcomponent, percent-encoded.
- [percentEncodedQuery](percentencodedquery.md) — The query subcomponent, percent-encoded.
- [URLQueryItem](../urlqueryitem.md) — A single name-value pair from the query portion of a URL.
- [percentEncodedUser](percentencodeduser.md) — The user subcomponent, percent-encoded.
