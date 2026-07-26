---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [macOS 12.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3v1cn'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3v1cn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28dynamicmember%3A%29-3v1cn.json'
content_hash: 'sha256:268925d72a41a840'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the attributed string key for a specified AppKit key path.

<sub>macOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.AppKitAttributes, T>) -> T where T : AttributedStringKey { get }
```

## See Also

### Accessing Framework Attribute Scopes

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3nor6.md>) — Returns the attributed string key for a specified Foundation key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3neai.md>) — Returns the attributed string key for a specified Foundation number format key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3q4ap.md>) — Returns the attributed string key for a specified SwiftUI key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-4yyyo.md>) — Returns the attributed string key for a specified UIKit key path.
