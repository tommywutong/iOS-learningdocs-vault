---
title: 'setAttributes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/setattributes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/setattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/setattributes%28_%3A%29.json'
content_hash: 'sha256:fd0b639661476ab7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# setAttributes(_:)

<sub>Instance Method</sub>

Sets the attributed string’s attributes to those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setAttributes(_ attributes: AttributeContainer)
```

## Parameters

- `attributes` — The attribute container with the attributes to apply.

## See Also

### Applying and Modifying Attributes

- [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replaceAttributes(_:with:)](<replaceattributes(__with_).md>) — Replaces occurrences of attributes in one attribute container with those in another attribute container.
- [AttributedStringAttributeMutation](../attributedstringattributemutation.md) — A protocol that defines in-place mutations for attributes in an attributed string.
