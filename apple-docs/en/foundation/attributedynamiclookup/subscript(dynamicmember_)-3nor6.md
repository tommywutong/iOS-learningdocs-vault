---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3nor6'
source_url: 'https://developer.apple.com/documentation/foundation/attributedynamiclookup/subscript(dynamicmember:)-3nor6'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedynamiclookup/subscript%28dynamicmember%3A%29-3nor6.json'
content_hash: 'sha256:6228380d10336667'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeDynamicLookup](../attributedynamiclookup.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns the attributed string key for a specified Foundation key path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<T>(dynamicMember keyPath: KeyPath<AttributeScopes.FoundationAttributes, T>) -> T where T : AttributedStringKey { get }
```

## See Also

### Accessing Framework Attribute Scopes

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3neai.md>) — Returns the attributed string key for a specified Foundation number format key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3q4ap.md>) — Returns the attributed string key for a specified SwiftUI key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-4yyyo.md>) — Returns the attributed string key for a specified UIKit key path.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3v1cn.md>) — Returns the attributed string key for a specified AppKit key path.
