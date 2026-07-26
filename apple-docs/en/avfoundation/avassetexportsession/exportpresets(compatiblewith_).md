---
title: 'exportPresets(compatibleWith:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetexportsession/exportpresets(compatiblewith:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportpresets(compatiblewith:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/exportpresets%28compatiblewith%3A%29.json'
content_hash: 'sha256:fbb46a79afaee189'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# exportPresets(compatibleWith:)

<sub>Type Method</sub>

Returns compatible export presets for the asset.

> [!warning] Deprecated
> Use [+ determineCompatibilityOfExportPreset:withAsset:outputFileType:completionHandler:](<determinecompatibility(ofexportpreset_with_outputfiletype_completionhandler_).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class func exportPresets(compatibleWith asset: AVAsset) -> [String]
```

## Parameters

- `asset` — An asset to export.

## Return Value

An array of compatible presets. See [Export presets](../export-presets.md) for preset values an asset export session supports.

## Discussion

Not all export presets are compatible with all assets. For example, video-only assets aren’t compatible with an audio-only preset. Call this method to determine the compatible presets for the asset you’re exporting.

> [!important] Important
> Load the asset’s [tracks](../avasset/tracks.md) property before calling this method to avoid blocking the calling thread.
