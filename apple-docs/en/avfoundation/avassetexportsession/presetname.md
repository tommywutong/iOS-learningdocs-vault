---
title: presetName
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetexportsession/presetname
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/presetname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/presetname.json'
content_hash: 'sha256:5b4ea0cd8068092d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# presetName

<sub>Instance Property</sub>

The name of the preset that the asset export session uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var presetName: String { get }
```

## Discussion

See [Export presets](../export-presets.md) for values an asset export session supports.

This property is key-value observable.

## See Also

### Accessing export presets

- [- determineCompatibleFileTypesWithCompletionHandler:](<determinecompatiblefiletypes(completionhandler_).md>) — Determines the output file types an asset export session supports writing in its current configuration.
- [+ allExportPresets](<allexportpresets().md>) — Returns all available export preset names.
- [+ determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:](<determinecompatibility(ofexportpreset_with_outputfiletype_completionhandler_).md>) — Determines an export preset’s compatibility to export the asset in a container of the output file type.
