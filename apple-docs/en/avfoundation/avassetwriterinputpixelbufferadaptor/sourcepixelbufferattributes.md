---
title: sourcePixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/sourcepixelbufferattributes.json'
content_hash: 'sha256:4f5a75a376ff8a79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md)

# sourcePixelBufferAttributes

<sub>Instance Property</sub>

The attributes of the pixel buffers that the pool contains.

> [!warning] Deprecated
> Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

## See Also

### Accessing the pool

- [pixelBufferPool](pixelbufferpool.md) — A pool of pixel buffers to append to the adaptor’s input. _(deprecated)_
