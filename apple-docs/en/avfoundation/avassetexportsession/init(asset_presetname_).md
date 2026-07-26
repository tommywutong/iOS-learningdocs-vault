---
title: 'init(asset:presetName:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/init(asset:presetname:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/init(asset:presetname:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/init%28asset%3Apresetname%3A%29.json'
content_hash: 'sha256:b01242e23c609b37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# init(asset:presetName:)

<sub>Initializer</sub>

Creates an export session with a preset configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init?(asset: AVAsset, presetName: String)
```

## Parameters

- `asset` — The asset to export.

- `presetName` — A string constant that specifies the preset template for the export. See [Export presets](../export-presets.md) for available values.

## See Also

### Creating an export session

- [Export presets](../export-presets.md) — Configure an export session to output media in standard sizes and formats.
