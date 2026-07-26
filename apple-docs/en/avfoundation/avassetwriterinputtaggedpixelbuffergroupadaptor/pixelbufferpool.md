---
title: pixelBufferPool
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/pixelbufferpool.json'
content_hash: 'sha256:5c3fa25505573fbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](../avassetwriterinputtaggedpixelbuffergroupadaptor.md)

# pixelBufferPool

<sub>Instance Property</sub>

A pixel buffer pool that vends and efficiently recycles the pixel buffers of tagged buffer groups.

> [!warning] Deprecated
> Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
var pixelBufferPool: CVPixelBufferPool? { get }
```

## Discussion

For maximum efficiency, create the pixel buffers of tagged buffer groups using this pool with the [CVPixelBufferPoolCreatePixelBuffer(_:_:_:)](<../../corevideo/cvpixelbufferpoolcreatepixelbuffer(______).md>) function.

The value of this property is `nil` before you call [- startWriting](<../avassetwriter/startwriting().md>) on the associated [AVAssetWriter](../avassetwriter.md) object. Query this property after writing starts to retrieve a `non-nil` value.

This property is not key value observable.

## See Also

### Configuring the buffer pool

- [sourcePixelBufferAttributes](sourcepixelbufferattributes.md) — The attributes of buffers that the adaptor’s pixel buffer pool vends. _(deprecated)_
