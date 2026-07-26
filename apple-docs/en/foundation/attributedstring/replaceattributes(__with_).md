---
title: 'replaceAttributes(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/replaceattributes(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/replaceattributes(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/replaceattributes%28_%3Awith%3A%29.json'
content_hash: 'sha256:26adbfbb3c0ac20c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# replaceAttributes(_:with:)

<sub>Instance Method</sub>

Replaces occurrences of attributes in one attribute container with those in another attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceAttributes(_ attributes: AttributeContainer, with others: AttributeContainer)
```

## Parameters

- `attributes` — The existing attributes to replace.

- `others` — The new attributes to apply.

## See Also

### Applying and Modifying Attributes

- [setAttributes(_:)](<setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [AttributedStringAttributeMutation](../attributedstringattributemutation.md) — A protocol that defines in-place mutations for attributes in an attributed string.
