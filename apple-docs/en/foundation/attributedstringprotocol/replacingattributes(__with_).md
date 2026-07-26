---
title: 'replacingAttributes(_:with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/replacingattributes(_:with:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/replacingattributes(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/replacingattributes%28_%3Awith%3A%29.json'
content_hash: 'sha256:73de0c82b1cda314'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# replacingAttributes(_:with:)

<sub>Instance Method</sub>

Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func replacingAttributes(_ attributes: AttributeContainer, with others: AttributeContainer) -> AttributedString
```

## Parameters

- `attributes` — The existing attributes to replace.

- `others` — The new attributes to apply.

## Return Value

An attributed string created by replacing occurrences of attributes in one attribute container with those in another attribute container.

## See Also

### Applying Attributes

- [settingAttributes(_:)](<settingattributes(__).md>) — Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.
- [mergingAttributes(_:mergePolicy:)](<mergingattributes(__mergepolicy_).md>) — Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
