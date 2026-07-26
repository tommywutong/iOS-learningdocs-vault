---
title: urlPathAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urlpathallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urlpathallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urlpathallowed.json'
content_hash: 'sha256:bfad4974c5b39b3f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlPathAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a path URL component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlPathAllowed: CharacterSet { get }
```

## Discussion

The path component of a URL is the component immediately following the host component (if present). It ends wherever the query or fragment component begins. For example, in the URL `http://www.example.com/index.php?key1=value1`, the path component is `/index.php`.

## See Also

### Getting Character Sets for URL Encoding

- [URLFragmentAllowedCharacterSet](urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [URLHostAllowedCharacterSet](urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [URLPasswordAllowedCharacterSet](urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [URLQueryAllowedCharacterSet](urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
- [URLUserAllowedCharacterSet](urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.
