---
title: PHPickerConfiguration.AssetRepresentationMode
framework: PhotosUI
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 13.0+, visionOS]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photosui/phpickerconfiguration-swift.struct/assetrepresentationmode
source_url: 'https://developer.apple.com/documentation/photosui/phpickerconfiguration-swift.struct/assetrepresentationmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photosui/phpickerconfiguration-swift.struct/assetrepresentationmode.json'
content_hash: 'sha256:a975be7ef4e8ef13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [PhotosUI](../../photosui.md) · [PHPickerConfiguration](../phpickerconfiguration-swift.struct.md)

# PHPickerConfiguration.AssetRepresentationMode

<sub>Enumeration</sub>

Constants identifying the mode the system uses when many representations exist for an asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum AssetRepresentationMode
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [PHPickerConfiguration.AssetRepresentationMode.automatic](assetrepresentationmode/automatic.md) — The system uses the best representation for the asset.
- [PHPickerConfiguration.AssetRepresentationMode.compatible](assetrepresentationmode/compatible.md) — The system uses the most compatible representation if possible.
- [PHPickerConfiguration.AssetRepresentationMode.current](assetrepresentationmode/current.md) — The system uses the current representation and avoids transcoding, if possible.

## See Also

### Selecting the preferred asset representation

- [preferredAssetRepresentationMode](preferredassetrepresentationmode.md) — A mode that determines which representation to use if an asset contains more than one.
