---
title: percentEncodedHost
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 8.0+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/urlcomponents/percentencodedhost
source_url: 'https://developer.apple.com/documentation/foundation/urlcomponents/percentencodedhost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/urlcomponents/percentencodedhost.json'
content_hash: 'sha256:5f99b5e875e06fbf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [URLComponents](../urlcomponents.md)

# percentEncodedHost

<sub>Instance Property</sub>

The host subcomponent, percent-encoded.

> [!warning] Deprecated
> Use [encodedHost](encodedhost.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedHost: String? { get set }
```

## Discussion

The getter for this property retains any percent encoding this component may have. Setting this properties assumes the component string is already correctly percent encoded. Attempting to set an incorrectly percent encoded string will cause a `fatalError`. Although ‘;’ is a legal path character, it is recommended that it be percent-encoded for best compatibility with `URL` (`String.addingPercentEncoding(withAllowedCharacters:)` will percent-encode any ‘;’ characters if you pass `CharacterSet.urlHostAllowed`).

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment subcomponent, percent-encoded.
- [percentEncodedPassword](percentencodedpassword.md) — The password subcomponent, percent-encoded.
- [percentEncodedPath](percentencodedpath.md) — The path subcomponent, percent-encoded.
- [percentEncodedQuery](percentencodedquery.md) — The query subcomponent, percent-encoded.
- [percentEncodedQueryItems](percentencodedqueryitems.md) — The query subcomponent, as an array of percent-encoded query items.
- [URLQueryItem](../urlqueryitem.md) — A single name-value pair from the query portion of a URL.
- [percentEncodedUser](percentencodeduser.md) — The user subcomponent, percent-encoded.
