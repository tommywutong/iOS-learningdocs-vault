---
title: percentEncodedQuery
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/percentencodedquery
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedquery'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/percentencodedquery.json'
content_hash: 'sha256:790d5d7f3ca5413c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# percentEncodedQuery

<sub>Instance Property</sub>

The query URL component expressed as a URL-encoded string, or `nil` if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedQuery: String? { get set }
```

## Discussion

For example, in the URL `http://www.example.com/index.php?key1=value1&key2=value2`, the query string is `key1=value1&key2=value2`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedHost](percentencodedhost.md) — The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present. _(deprecated)_
- [percentEncodedPassword](percentencodedpassword.md) — The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedPath](percentencodedpath.md) — The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedUser](percentencodeduser.md) — The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
