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
doc_path: '/documentation/foundation/attributedsubstring/setattributes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedsubstring/setattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedsubstring/setattributes%28_%3A%29.json'
content_hash: 'sha256:135ef291218c2e5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedSubstring](../attributedsubstring.md)

# setAttributes(_:)

<sub>Instance Method</sub>

Sets the attributed substring’s attributes to those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func setAttributes(_ attributes: AttributeContainer)
```

## Parameters

- `attributes` — The attribute container with the attributes to apply.

## See Also

### Applying and Modifying Attributes

- [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replaceAttributes(_:with:)](<replaceattributes(__with_).md>) — Replaces the attributed substring’s attributes with those in a specified attribute container.
