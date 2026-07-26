---
title: 'mergingAttributes(_:mergePolicy:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstringprotocol/mergingattributes(_:mergepolicy:)'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstringprotocol/mergingattributes(_:mergepolicy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstringprotocol/mergingattributes%28_%3Amergepolicy%3A%29.json'
content_hash: 'sha256:c7e416887d27b76b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedStringProtocol](../attributedstringprotocol.md)

# mergingAttributes(_:mergePolicy:)

<sub>Instance Method</sub>

Returns an attributed string by merging the attributed string’s attributes with those in a specified attribute container.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func mergingAttributes(_ attributes: AttributeContainer, mergePolicy: AttributedString.AttributeMergePolicy = .keepNew) -> AttributedString
```

## Parameters

- `attributes` — The attribute container with the attributes to merge.

- `mergePolicy` — A policy to use when resolving conflicts between this string’s attributes and those in `attributes`.

## Return Value

An attributed string from merging the attributed string’s attributes with those in a specified attribute container. In cases where the same attribute exists in both the source string and `attributes`, the `mergePolicy` determines which value the returned string uses.

## See Also

### Applying Attributes

- [settingAttributes(_:)](<settingattributes(__).md>) — Returns an attributed string by setting the attributed string’s attributes to those in a specified attribute container.
- [AttributeMergePolicy](../attributedstring/attributemergepolicy.md) — An enumeration of behaviors to apply when merging attributes.
- [replacingAttributes(_:with:)](<replacingattributes(__with_).md>) — Returns an attributed string by replacing occurrences of attributes in one attribute container with those in another attribute container.
