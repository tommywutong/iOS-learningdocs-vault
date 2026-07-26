---
title: pixelBufferPool
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver/pixelbufferpool.json'
content_hash: 'sha256:2a562fd174fb32bc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVAssetWriterInput](../../avassetwriterinput.md) · [TaggedPixelBufferGroupReceiver](../taggedpixelbuffergroupreceiver.md)

# pixelBufferPool

<sub>Instance Property</sub>

A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var pixelBufferPool: CVMutablePixelBuffer.Pool? { get }
```

## See Also

### Accessing the pixel buffer pool

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.
