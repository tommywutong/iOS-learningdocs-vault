---
title: 'exportSessionWithAsset:presetName:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetexportsession/exportsessionwithasset:presetname:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetexportsession/exportsessionwithasset:presetname:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetexportsession/exportsessionwithasset%3Apresetname%3A.json'
content_hash: 'sha256:6c0d23e6721614ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetExportSession](../avassetexportsession.md)

# exportSessionWithAsset:presetName:

<sub>Type Method</sub>

Returns a new asset export session that uses the specified preset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) exportSessionWithAsset:(AVAsset *) asset presetName:(NSString *) presetName;
```

## Parameters

- `asset` — The asset to export.

- `presetName` — A string constant that specifies the preset template for the export. See [Export presets](../export-presets.md) for values an asset export session supports.

## Return Value

An asset export session.

## See Also

### Creating an export session

- [- initWithAsset:presetName:](<init(asset_presetname_).md>) — Creates an export session with a preset configuration.
- [Export presets](../export-presets.md) — Configure an export session to output media in standard sizes and formats.
