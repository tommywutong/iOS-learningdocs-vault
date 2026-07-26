---
title: 'subscript(_:)'
framework: Foundation
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedsubstring/subscript(_:)-2hp64'
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/subscript(_:)-2hp64'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/subscript%28_%3A%29-2hp64.json'
content_hash: 'sha256:ca733b942c28bcc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Returns an attribute value that corresponds to an attributed string key.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency subscript<K>(_: K.Type) -> K.Value? where K : AttributedStringKey, K.Value : Sendable { get set }
```

## Discussion

This subscript returns `nil` unless the specified attribute exists, and is present and identical for the entire attributed string or substring. To find portions of the string with consistent attributes, use the [runs](runs.md) property.

Getting or setting stringwide attributes with this subscript has `O(n)` behavior in the worst case, where `n` is the number of runs.

## See Also

### Accessing Whole-Substring Attributes

- [subscript(dynamicMember:)](<subscript(dynamicmember_)-3o8o1.md>) — Returns an attribute value that a key path indicates.
- [AttributeDynamicLookup](../attributedynamiclookup.md) — A type to support dynamic member lookup of attributes and containers.
- [subscript(dynamicMember:)](<subscript(dynamicmember_)-548k0.md>) — Returns a scoped attribute container that a key path indicates.
- [ScopedAttributeContainer](../scopedattributecontainer.md) — An attribute container that allows dynamic member lookup of its contents within the specified attribute scope.
