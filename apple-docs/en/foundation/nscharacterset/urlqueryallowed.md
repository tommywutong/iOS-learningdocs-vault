---
title: urlQueryAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urlqueryallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urlqueryallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urlqueryallowed.json'
content_hash: 'sha256:6a9d235dcfb69ab4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlQueryAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a query URL component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlQueryAllowed: CharacterSet { get }
```

## Discussion

The query component of a URL is the component immediately following a question mark (`?`). For example, in the URL `http://www.example.com/index.php?key1=value1#jumpLink`, the query component is `key1=value1`.

## See Also

### Getting Character Sets for URL Encoding

- [URLFragmentAllowedCharacterSet](urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [URLHostAllowedCharacterSet](urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [URLPasswordAllowedCharacterSet](urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [URLPathAllowedCharacterSet](urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [URLUserAllowedCharacterSet](urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.
