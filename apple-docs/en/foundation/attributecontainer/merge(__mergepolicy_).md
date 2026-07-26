---
title: 'merge(_:mergePolicy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/merge(_:mergepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/merge(_:mergepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/merge%28_%3Amergepolicy%3A%29.json'
content_hash: 'sha256:267e8cea137c027f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# merge(_:mergePolicy:)

<sub>Instance Method</sub>

Merges the container’s attributes with those in another attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func merge(_ other: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew)
```

## Parameters

- `other` — The attribute container with the attributes to merge.

- `mergePolicy` — A policy to use when resolving conflicts between this string’s attributes and those in `other`.

## See Also

### Modifying Attributes

- [merging(_:mergePolicy:)](<merging(__mergepolicy_).md>) — Returns an attribute container by merging the container’s attributes with those in another attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
