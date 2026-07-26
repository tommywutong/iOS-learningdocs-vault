---
title: preferredAssetRepresentationMode
framework: PhotosUI
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/preferredassetrepresentationmode
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/preferredassetrepresentationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/preferredassetrepresentationmode.json'
content_hash: 'sha256:756bfaefe82d4c53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# preferredAssetRepresentationMode

<sub>Instance Property</sub>

A mode that determines which representation to use if an asset contains more than one.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var preferredAssetRepresentationMode: PHPickerConfiguration.AssetRepresentationMode
```

## Discussion

An asset can contain many representations under the same uniform type identifier, or you can prefer a specific format. This mode determines which representation an [NSItemProvider](../../foundation/nsitemprovider.md) uses if many exist.

The system may perform additional transcoding to convert the asset you request to the compatable representation. Use [PHPickerConfiguration.AssetRepresentationMode.current](assetrepresentationmode/current.md) to avoid transcoding, if possible.

## See Also

### Selecting the preferred asset representation

- [AssetRepresentationMode](assetrepresentationmode.md) — Constants identifying the mode the system uses when many representations exist for an asset.
