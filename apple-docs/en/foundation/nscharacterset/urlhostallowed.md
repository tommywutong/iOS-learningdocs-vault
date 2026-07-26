---
title: urlHostAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urlhostallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urlhostallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urlhostallowed.json'
content_hash: 'sha256:7355d0f39915d299'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlHostAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a host URL subcomponent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlHostAllowed: CharacterSet { get }
```

## Discussion

The host component of a URL is usually the component immediately after the first two leading slashes. If the URL contains a username and password, the host component is the component after the `@` sign. For example, in the URL `http://username:password@www.example.com/index.html`, the host component is `www.example.com`.

## See Also

### Getting Character Sets for URL Encoding

- [URLFragmentAllowedCharacterSet](urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [URLPasswordAllowedCharacterSet](urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [URLPathAllowedCharacterSet](urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [URLQueryAllowedCharacterSet](urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
- [URLUserAllowedCharacterSet](urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.
