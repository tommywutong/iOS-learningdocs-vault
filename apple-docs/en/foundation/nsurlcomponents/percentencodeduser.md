---
title: percentEncodedUser
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/percentencodeduser
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodeduser'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/percentencodeduser.json'
content_hash: 'sha256:d2f5874ca27f5364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# percentEncodedUser

<sub>Instance Property</sub>

The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedUser: String? { get set }
```

## Discussion

For example, in the URL `http://username:password@www.example.com/index.html`, the user is `username`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedHost](percentencodedhost.md) — The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present. _(deprecated)_
- [percentEncodedPassword](percentencodedpassword.md) — The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedPath](percentencodedpath.md) — The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedQuery](percentencodedquery.md) — The query URL component expressed as a URL-encoded string, or `nil` if not present.
