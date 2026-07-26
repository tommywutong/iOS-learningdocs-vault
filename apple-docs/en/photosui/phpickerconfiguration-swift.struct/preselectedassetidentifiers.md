---
title: preselectedAssetIdentifiers
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/preselectedassetidentifiers
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/preselectedassetidentifiers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/preselectedassetidentifiers.json'
content_hash: 'sha256:188e74e7cd7076db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# preselectedAssetIdentifiers

<sub>Instance Property</sub>

An array of asset identifiers to preselect in the picker.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var preselectedAssetIdentifiers: [String] { get set }
```

## Discussion

Preselection works only when initializing a [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md) object with a photo library. Otherwise, the system returns an error.

The number of preselected asset identifiers can exceed your selection limit. The system disables the done action until the selection count becomes lower than [selectionLimit](selectionlimit.md).

Additionally, when providing preselected identifiers:

- Results include all preselected identifiers when canceling the picker.
- Results don’t include item providers for preselected assets that remain selected.
- When deselecting all assets, the system keeps the done action enabled.
