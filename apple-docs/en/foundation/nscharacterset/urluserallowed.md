---
title: urlUserAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urluserallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urluserallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urluserallowed.json'
content_hash: 'sha256:e984d7817b72fb12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlUserAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a user URL subcomponent.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlUserAllowed: CharacterSet { get }
```

## Discussion

The user component of a URL is an optional component that precedes the host component, and ends at either a colon (if a password is specified) or an `@` sign (if no password is specified). For example, in the URL `http://username:password@www.example.com/index.html`, the user component is `username`.

## See Also

### Getting Character Sets for URL Encoding

- [URLFragmentAllowedCharacterSet](urlfragmentallowed.md) — Returns the character set for characters allowed in a fragment URL component.
- [URLHostAllowedCharacterSet](urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [URLPasswordAllowedCharacterSet](urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [URLPathAllowedCharacterSet](urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [URLQueryAllowedCharacterSet](urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
