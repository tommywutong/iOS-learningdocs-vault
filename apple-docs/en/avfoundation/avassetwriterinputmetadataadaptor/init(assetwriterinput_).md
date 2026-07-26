---
title: 'init(assetWriterInput:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputmetadataadaptor/init(assetwriterinput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputmetadataadaptor/init(assetwriterinput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputmetadataadaptor/init%28assetwriterinput%3A%29.json'
content_hash: 'sha256:857e0da78659474e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputMetadataAdaptor](../avassetwriterinputmetadataadaptor.md)

# init(assetWriterInput:)

<sub>Initializer</sub>

Creates a metadata group adaptor to append timed metadata groups to write to an output file.

> [!warning] Deprecated
> Use AVAssetWriter.inputMetadataReceiver(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(assetWriterInput input: AVAssetWriterInput)
```

## Parameters

- `input` — The metadata input to which to append groups of timed metadata.
