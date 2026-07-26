---
title: urlFragmentAllowed
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/urlfragmentallowed
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/urlfragmentallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/urlfragmentallowed.json'
content_hash: 'sha256:27287dc5f140e36b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# urlFragmentAllowed

<sub>Type Property</sub>

Returns the character set for characters allowed in a fragment URL component.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var urlFragmentAllowed: CharacterSet { get }
```

## Discussion

The fragment component of a URL is the component after a `#` symbol. For example, in the URL `http://www.example.com/index.html#jumpLocation`, the fragment is `jumpLocation`.

## See Also

### Getting Character Sets for URL Encoding

- [URLHostAllowedCharacterSet](urlhostallowed.md) — Returns the character set for characters allowed in a host URL subcomponent.
- [URLPasswordAllowedCharacterSet](urlpasswordallowed.md) — Returns the character set for characters allowed in a password URL subcomponent.
- [URLPathAllowedCharacterSet](urlpathallowed.md) — Returns the character set for characters allowed in a path URL component.
- [URLQueryAllowedCharacterSet](urlqueryallowed.md) — Returns the character set for characters allowed in a query URL component.
- [URLUserAllowedCharacterSet](urluserallowed.md) — Returns the character set for characters allowed in a user URL subcomponent.
