---
title: 'merging(_:mergePolicy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributecontainer/merging(_:mergepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributecontainer/merging(_:mergepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributecontainer/merging%28_%3Amergepolicy%3A%29.json'
content_hash: 'sha256:d64c9c057411a9fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributeContainer](../attributecontainer.md)

# merging(_:mergePolicy:)

<sub>Instance Method</sub>

Returns an attribute container by merging the container’s attributes with those in another attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func merging(_ other: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew) -> AttributeContainer
```

## Parameters

- `other` — The attribute container with the attributes to merge.

- `mergePolicy` — A policy to use when resolving conflicts between this string’s attributes and those in `other`.

## Return Value

An attribute container created by merging the source container’s attributes with those in another attribute container.

## See Also

### Modifying Attributes

- [merge(_:mergePolicy:)](<merge(__mergepolicy_).md>) — Merges the container’s attributes with those in another attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
