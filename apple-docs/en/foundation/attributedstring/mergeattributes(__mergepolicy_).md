---
title: 'mergeAttributes(_:mergePolicy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/mergeattributes(_:mergepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/mergeattributes(_:mergepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/mergeattributes%28_%3Amergepolicy%3A%29.json'
content_hash: 'sha256:9e5b27b82a225df3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# mergeAttributes(_:mergePolicy:)

<sub>Instance Method</sub>

Merges the attributed string’s attributes with those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func mergeAttributes(_ attributes: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew)
```

## Parameters

- `attributes` — The attribute container with the attributes to merge.

- `mergePolicy` — A policy to use when resolving conflicts between this string’s attributes and those in `attributes`.

## See Also

### Applying and Modifying Attributes

- [setAttributes(_:)](<setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [AttributeMergePolicy](attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replaceAttributes(_:with:)](<replaceattributes(__with_).md>) — Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [AttributedStringAttributeMutation](../attributedstringattributemutation.md) — A protocol that defines in-place mutations for attributes in an attributed string.
