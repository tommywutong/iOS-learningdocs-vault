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
doc_path: '/documentation/foundation/attributedstring/subscript(dynamicmember:)-34zdf'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/subscript(dynamicmember:)-34zdf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/subscript%28dynamicmember%3A%29-34zdf.json'
content_hash: 'sha256:2dd219f4f13fb9ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# subscript(dynamicMember:)

<sub>Instance Subscript</sub>

Returns an attribute value that a key path indicates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(dynamicMember keyPath: KeyPath<AttributeDynamicLookup, K>) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## Discussion

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of the string with consistent attributes, use the [runs](runs-swift.property.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

### Accessing Whole-String Attributes

- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-9modq.md>) — Returns a scoped attribute container that a key path indicates.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
