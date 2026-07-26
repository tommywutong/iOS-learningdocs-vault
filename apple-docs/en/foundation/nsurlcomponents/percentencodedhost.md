---
title: percentEncodedHost
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+（27.0 起废弃）, iPadOS 7.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.9+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsurlcomponents/percentencodedhost
source_url: 'https://developer.apple.com/documentation/foundation/nsurlcomponents/percentencodedhost'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsurlcomponents/percentencodedhost.json'
content_hash: 'sha256:a90d9b3d2f1db48d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSURLComponents](../nsurlcomponents.md)

# percentEncodedHost

<sub>Instance Property</sub>

The host URL subcomponent expressed as a URL-encoded string, or `nil` if not present.

> [!warning] Deprecated
> Use encodedHost instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var percentEncodedHost: String? { get set }
```

## Discussion

For example, in the URL `http://www.example.com/index.html`, the host is `www.example.com`.

If you set this value to something that is not a valid, percent-encoded string, this class throws an exception.

## See Also

### Accessing components in URL-encoded format

- [percentEncodedFragment](percentencodedfragment.md) — The fragment URL component (the part after a `#` symbol) expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedPassword](percentencodedpassword.md) — The password URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedPath](percentencodedpath.md) — The path URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedQuery](percentencodedquery.md) — The query URL component expressed as a URL-encoded string, or `nil` if not present.
- [percentEncodedUser](percentencodeduser.md) — The username URL subcomponent expressed as a URL-encoded string, or `nil` if not present.
