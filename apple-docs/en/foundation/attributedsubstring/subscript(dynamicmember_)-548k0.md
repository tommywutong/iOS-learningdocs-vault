---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedsubstring/subscript(dynamicmember:)-548k0'
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/subscript(dynamicmember:)-548k0'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/subscript%28dynamicmember%3A%29-548k0.json'
content_hash: 'sha256:b76e6957e6b2f7cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a scoped attribute container that a key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```

## Discussion

Use this subscript when you need to work with an explicit attribute scope. For example, the SwiftUI [foregroundColor](../attributescopes/swiftuiattributes/foregroundcolor.md) attribute overrides the attribute in the AppKit and UIKit scopes with the same name. If you work with both the SwiftUI and UIKit scopes, you can use the syntax `myAttributedSubstring.uiKit.foregroundColor` to disambiguate and explicitly use the UIKit attribute.

The attribute container that this method returns contains only attributes that exist, and are present and identical for the entire attributed string. To find portions of the string with consistent attributes, use the [runs](runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

### Accessing Whole-Substring Attributes

- [subscript(_:)](<subscript(__)-2hp64.md>) — Returns an attribute value that corresponds to an attributed string key.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3o8o1.md>) — Returns an attribute value that a key path indicates.
- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
