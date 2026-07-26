---
title: sourcePixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/sourcepixelbufferattributes.json'
content_hash: 'sha256:f36dd53a732ec65a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](../avassetwriterinputtaggedpixelbuffergroupadaptor.md)

# sourcePixelBufferAttributes

<sub>Instance Property</sub>

The attributes of buffers that the adaptor’s pixel buffer pool vends.

> [!warning] Deprecated
> Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var sourcePixelBufferAttributes: [String : any Sendable]? { get }
```

## Discussion

The value of this property is a dictionary containing pixel buffer attribute keys defined in `<CoreVideo/CVPixelBuffer.h>`.

## See Also

### Configuring the buffer pool

- [pixelBufferPool](pixelbufferpool.md) — A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups. _(deprecated)_
