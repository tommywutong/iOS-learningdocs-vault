---
title: urlPasswordAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urlpasswordallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urlpasswordallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urlpasswordallowed.json'
content_hash: 'sha256:fc895437f83a76bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlPasswordAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a password URL subcomponent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlPasswordAllowed: CharacterSet { get }
```

## Discussion

The password component of a URL is the component immediately following the colon after the username component of the URL, and ends at the `@` sign. For example, in the URL `http://username:password@www.example.com/index.html`, the pass component is `password`.

## See Also

### Getting Character Sets for URL Encoding

- [URLFragmentAllowedCharacterSet](urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [URLHostAllowedCharacterSet](urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [URLPathAllowedCharacterSet](urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [URLQueryAllowedCharacterSet](urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
- [URLUserAllowedCharacterSet](urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.
