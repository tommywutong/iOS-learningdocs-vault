---
title: percentEncodedPassword
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsurlcomponents/percentencodedpassword
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedpassword'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/percentencodedpassword.json'
content_hash: 'sha256:504f3691d10c00d0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# percentEncodedPassword

<sub>Instance Property</sub>

The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedPassword: String? { get set }
```

## Discussion

For example, in the URL `http://username:password@www.example.com/index.html`, the password is `password`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedHost](percentencodedhost.md) — The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present. _(deprecated)_
- [percentEncodedPath](percentencodedpath.md) — The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedQuery](percentencodedquery.md) — The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedUser](percentencodeduser.md) — The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
