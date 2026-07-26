---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/subscript(_:)-4thnp'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/subscript(_:)-4thnp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/subscript%28_%3A%29-4thnp.json'
content_hash: 'sha256:7668d4362446e292'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns an attribute value that corresponds to an attributed string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## Discussion

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of an attributed string with consistent attributes, use the [runs](../attributedstring/runs-swift.property.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## Default Implementations

### AttributedStringProtocol Implementations

- [subscript(_:)](<subscript(__)-67hgv.md>) — Returns a discontiguous substring of this attributed string using a set of ranges to indicate the discontiguous substring bounds.

## See Also

### Accessing Whole-String Attributes

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-2wake.md>) — Returns an attribute value that a key path indicates.
- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-55pcu.md>) — Returns a scoped attribute container that a key path indicates.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
