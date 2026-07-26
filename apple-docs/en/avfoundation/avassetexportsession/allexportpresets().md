---
title: allExportPresets()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/allexportpresets()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/allexportpresets()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/allexportpresets%28%29.json'
content_hash: 'sha256:f6f510e79355d6bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# allExportPresets()

<sub>Type Method</sub>

Returns all available export preset names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func allExportPresets() -> [String]
```

## Return Value

See [Export presets](../export-presets.md) for values an asset export session supports.

## Discussion

Not all presets are compatible with all assets.

## See Also

### Accessing export presets

- [presetName](presetname.md) — The name of the preset that the asset export session uses.
- [- determineCompatibleFileTypesWithCompletionHandler:](<determinecompatiblefiletypes(completionhandler_).md>) — Determines the output file types an asset export session supports writing in its current configuration.
- [+ determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:](<determinecompatibility(ofexportpreset_with_outputfiletype_completionhandler_).md>) — Determines an export preset’s compatibility to export the asset in a container of the output file type.
