---
title: 'init(assetWriterInput:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+（27.0 起废弃）, iPadOS 18.0+（27.0 起废弃）, Mac Catalyst 15.0+（27.0 起废弃）, macOS 12.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputcaptionadaptor/init(assetwriterinput:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputcaptionadaptor/init(assetwriterinput:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputcaptionadaptor/init%28assetwriterinput%3A%29.json'
content_hash: 'sha256:fa067f4677a3eb1e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputCaptionAdaptor](../avassetwriterinputcaptionadaptor.md)

# init(assetWriterInput:)

<sub>Initializer</sub>

Creates a new caption adaptor that writes to the specified asset writer input.

> [!warning] Deprecated
> Use AVAssetWriter.inputCaptionReceiver(for:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
init(assetWriterInput input: AVAssetWriterInput)
```

## Parameters

- `input` — The asset writer input.
