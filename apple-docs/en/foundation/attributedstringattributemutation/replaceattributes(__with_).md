---
title: 'replaceAttributes(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringattributemutation/replaceattributes(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringattributemutation/replaceattributes(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringattributemutation/replaceattributes%28_%3Awith%3A%29.json'
content_hash: 'sha256:3ac505d0299238b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringAttributeMutation](../attributedstringattributemutation.md)

# replaceAttributes(_:with:)

<sub>Instance Method</sub>

Replaces the attributed string’s attributes with those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func replaceAttributes(_ attributes: AttributeContainer, with others: AttributeContainer)
```

## Parameters

- `attributes` — The existing attributes to replace.

- `others` — The new attributes to apply.

## See Also

### Mutating the String’s Attributes

- [setAttributes(_:)](<setattributes(__).md>) — Sets the attributed string’s attributes to those in a specified attribute container.
- [mergeAttributes(_:mergePolicy:)](<mergeattributes(__mergepolicy_).md>) — Merges the attributed string’s attributes with those in a specified attribute container.
