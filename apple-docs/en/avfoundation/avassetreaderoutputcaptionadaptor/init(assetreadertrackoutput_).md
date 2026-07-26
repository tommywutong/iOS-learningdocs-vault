---
title: 'init(assetReaderTrackOutput:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetreaderoutputcaptionadaptor/init(assetreadertrackoutput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetreaderoutputcaptionadaptor/init(assetreadertrackoutput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetreaderoutputcaptionadaptor/init%28assetreadertrackoutput%3A%29.json'
content_hash: 'sha256:d356cd84d09874cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetReaderOutputCaptionAdaptor](../avassetreaderoutputcaptionadaptor.md)

# init(assetReaderTrackOutput:)

<sub>Initializer</sub>

Creates a caption adaptor that reads from a track output.

> [!warning] Deprecated
> Use AVAssetReader.outputCaptionProvider(for:validationDelegate:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(assetReaderTrackOutput trackOutput: AVAssetReaderTrackOutput)
```

## Parameters

- `trackOutput` — The track output from which the system reads captions.
