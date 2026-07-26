---
title: pixelBufferPool
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputpixelbufferadaptor/pixelbufferpool
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/pixelbufferpool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/pixelbufferpool.json'
content_hash: 'sha256:9ed644cd6d377b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md)

# pixelBufferPool

<sub>Instance Property</sub>

A pool of pixel buffers to append to the adaptor’s input.

> [!warning] Deprecated
> Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelBufferPool: CVPixelBufferPool? { get }
```

## Discussion

For maximum efficiency, you should create [CVPixelBuffer](../../corevideo/cvpixelbuffer-q2e.md) objects for [- appendPixelBuffer:withPresentationTime:](<append(__withpresentationtime_).md>) by using this pool with the [CVPixelBufferPoolCreatePixelBuffer(_:_:_:)](<../../corevideo/cvpixelbufferpoolcreatepixelbuffer(______).md>) function.

This value is `nil` prior to calling [- startSessionAtSourceTime:](<../avassetwriter/startsession(atsourcetime_).md>)on the associated [AVAssetWriter](../avassetwriter.md) object.

This property is key-value observable.

## See Also

### Accessing the pool

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The attributes of the pixel buffers that the pool contains. _(deprecated)_
