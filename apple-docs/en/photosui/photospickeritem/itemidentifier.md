---
title: itemIdentifier
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/photospickeritem/itemidentifier
source_url: 'https://developer.apple.com/documentation/photosui/photospickeritem/itemidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/photospickeritem/itemidentifier.json'
content_hash: 'sha256:cd3c760d09fdaf78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PhotosPickerItem](../photospickeritem.md)

# itemIdentifier

<sub>Instance Property</sub>

The local identifier of the item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var itemIdentifier: String? { get }
```

## Discussion

This value is `nil` if you create a Photos picker without a photo library.

## See Also

### Inspecting a picker item

- [supportedContentTypes](supportedcontenttypes.md) — The content types the item supports in order of the most preferred to the least.
