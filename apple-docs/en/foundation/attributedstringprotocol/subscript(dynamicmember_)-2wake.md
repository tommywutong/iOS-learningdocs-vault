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
doc_path: '/documentation/foundation/attributedstringprotocol/subscript(dynamicmember:)-2wake'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(dynamicmember:)-2wake'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/subscript%28dynamicmember%3A%29-2wake.json'
content_hash: 'sha256:005150da5c78d28e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns an attribute value that a key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## Discussion

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of an attributed string with consistent attributes, use the [runs](runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

### Accessing Whole-String Attributes

- [subscript(_:)](<subscript(__)-4thnp.md>) — Returns an attribute value that corresponds to an attributed string key.
- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-55pcu.md>) — Returns a scoped attribute container that a key path indicates.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
