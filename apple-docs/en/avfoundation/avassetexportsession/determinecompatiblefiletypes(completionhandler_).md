---
title: 'determineCompatibleFileTypes(completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/determinecompatiblefiletypes(completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/determinecompatiblefiletypes(completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/determinecompatiblefiletypes%28completionhandler%3A%29.json'
content_hash: 'sha256:bb2d9e1155f440b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# determineCompatibleFileTypes(completionHandler:)

<sub>Instance Method</sub>

Determines the output file types an asset export session supports writing in its current configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func determineCompatibleFileTypes(completionHandler handler: @escaping @Sendable ([AVFileType]) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var compatibleFileTypes: [AVFileType] { get async }
```

## Parameters

- `handler` — A callback the system passes an array of [AVFileType](../avfiletype.md) structures when it determines the compatible file types.

## See Also

### Accessing export presets

- [presetName](presetname.md) — The name of the preset that the asset export session uses.
- [+ allExportPresets](<allexportpresets().md>) — Returns all available export preset names.
- [+ determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:](<determinecompatibility(ofexportpreset_with_outputfiletype_completionhandler_).md>) — Determines an export preset’s compatibility to export the asset in a container of the output file type.
