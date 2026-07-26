---
title: percentEncodedUser
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/urlcomponents/percentencodeduser
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/percentencodeduser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/percentencodeduser.json'
content_hash: 'sha256:f806f797193d27d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# percentEncodedUser

<sub>Instance Property</sub>

The user subcomponent, percent-encoded.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedUser: String? { get set }
```

## Discussion

The getter for this property retains any percent encoding this component may have. Setting this properties assumes the component string is already correctly percent encoded. Attempting to set an incorrectly percent encoded string will cause a `fatalError`. Although ‘;’ is a legal path character, it is recommended that it be percent-encoded for best compatibility with `URL` (`String.addingPercentEncoding(withAllowedCharacters:)` will percent-encode any ‘;’ characters if you pass `CharacterSet.urlUserAllowed`).

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment subcomponent, percent-encoded.
- [percentEncodedHost](percentencodedhost.md) — The host subcomponent, percent-encoded. _(deprecated)_
- [percentEncodedPassword](percentencodedpassword.md) — The password subcomponent, percent-encoded.
- [percentEncodedPath](percentencodedpath.md) — The path subcomponent, percent-encoded.
- [percentEncodedQuery](percentencodedquery.md) — The query subcomponent, percent-encoded.
- [percentEncodedQueryItems](percentencodedqueryitems.md) — The query subcomponent, as an array of percent-encoded query items.
- [URLQueryItem](../urlqueryitem.md) — A single name-value pair from the query portion of a URL.
