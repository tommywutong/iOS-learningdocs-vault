---
title: 'subscript(dynamicMember:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/subscript(dynamicmember:)-55pcu'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(dynamicmember:)-55pcu'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/subscript%28dynamicmember%3A%29-55pcu.json'
content_hash: 'sha256:cf21281c44cb5b81'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns a scoped attribute container that a key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript<S>(dynamicMember keyPath: KeyPath<AttributeScopes, S.Type>) -> ScopedAttributeContainer<S> where S : AttributeScope { get set }
```

## Discussion

Use this subscript when you need to work with an explicit attribute scope. For example, the SwiftUI [foregroundColor](../attributescopes/swiftuiattributes/foregroundcolor.md) attribute overrides the attribute in the AppKit and UIKit scopes with the same name. If you work with both the SwiftUI and UIKit scopes, you can use the syntax `myAttributedString.uiKit.foregroundColor` to disambiguate and explicitly use the UIKit attribute.

The attribute container that this method returns contains only attributes that exist, and are present and identical for the entire attributed string. To find portions of the string with consistent attributes, use the [runs](runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

### Accessing Whole-String Attributes

- [subscript(_:)](<subscript(__)-4thnp.md>) — Returns an attribute value that corresponds to an attributed string key.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-2wake.md>) — Returns an attribute value that a key path indicates.
- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
