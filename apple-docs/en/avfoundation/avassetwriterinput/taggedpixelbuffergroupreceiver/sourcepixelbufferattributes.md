---
title: sourcePixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.json'
content_hash: 'sha256:b42a5348e6b911f3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [TaggedPixelBufferGroupReceiver](../taggedpixelbuffergroupreceiver.md)

# sourcePixelBufferAttributes

<sub>Instance Property</sub>

The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var sourcePixelBufferAttributes: CVPixelBufferCreationAttributes? { get }
```

## See Also

### Accessing the pixel buffer pool

- [pixelBufferPool](pixelbufferpool.md) — A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
