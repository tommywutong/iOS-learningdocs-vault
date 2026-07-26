---
title: 'determineCompatibility(ofExportPreset:with:outputFileType:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/determinecompatibility(ofexportpreset:with:outputfiletype:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/determinecompatibility%28ofexportpreset%3Awith%3Aoutputfiletype%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:040656166be5fb48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# determineCompatibility(ofExportPreset:with:outputFileType:completionHandler:)

<sub>Type Method</sub>

Determines an export preset’s compatibility to export the asset in a container of the output file type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func determineCompatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType: AVFileType?, completionHandler handler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func compatibility(ofExportPreset presetName: String, with asset: AVAsset, outputFileType: AVFileType?) async -> Bool
```

## Parameters

- `presetName` — The name of the preset whose compatibility you want to test. See [Export presets](../export-presets.md) for preset values an asset export session supports.

- `asset` — The asset to export.

- `outputFileType` — The file type of the output container.

- `handler` — A callback the system passes a Boolean result when it determines the compatibility of the preset.

## See Also

### Accessing export presets

- [presetName](presetname.md) — The name of the preset that the asset export session uses.
- [- determineCompatibleFileTypesWithCompletionHandler:](<determinecompatiblefiletypes(completionhandler_).md>) — Determines the output file types an asset export session supports writing in its current configuration.
- [+ allExportPresets](<allexportpresets().md>) — Returns all available export preset names.
