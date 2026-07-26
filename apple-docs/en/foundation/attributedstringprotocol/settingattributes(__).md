---
title: 'settingAttributes(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/settingattributes(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/settingattributes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/settingattributes%28_%3A%29.json'
content_hash: 'sha256:802b0fe9ae83f8f4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# settingAttributes(_:)

<sub>Instance Method</sub>

Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func settingAttributes(_ attributes: AttributeContainer) -> AttributedString
```

## Parameters

- `attributes` — The attribute container with the attributes to apply.

## Return Value

An attributed string from setting the attributed string’s attributes to those in a specified attribute container.

## See Also

### Applying Attributes

- [mergingAttributes(_:mergePolicy:)](<mergingattributes(__mergepolicy_).md>) — Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replacingAttributes(_:with:)](<replacingattributes(__with_).md>) — Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.
