---
title: 'init(assetWriterInput:sourcePixelBufferAttributes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/init(assetwriterinput:sourcepixelbufferattributes:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/init(assetwriterinput:sourcepixelbufferattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputtaggedpixelbuffergroupadaptor/init%28assetwriterinput%3Asourcepixelbufferattributes%3A%29.json'
content_hash: 'sha256:533b8ee97d69e72b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputTaggedPixelBufferGroupAdaptor](../avassetwriterinputtaggedpixelbuffergroupadaptor.md)

# init(assetWriterInput:sourcePixelBufferAttributes:)

<sub>Initializer</sub>

Creates an object that appends tagged buffer groups to an asset writer input.

> [!warning] Deprecated
> Use AVAssetWriter.inputTaggedPixelBufferGroupReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

## Parameters

- `input` — An asset writer input, that handles media data of type [AVMediaTypeVideo](../avmediatype/video.md), to use for appending tagged buffer groups. It’s an error to initialize an adaptor with an asset writer input that is already attached to another instance of tagged pixel buffer group adaptor, or to one th that progresses beyond its [AVAssetWriterStatusUnknown](../avassetwriter/status-swift.enum/unknown.md) state.

- `sourcePixelBufferAttributes` — Specifies the attributes of pixel buffers that the adaptor’s pixel buffer pool vends. If your app doesn’t require a pixel buffer pool, this this value to `nil`.

## Discussion

To take advantage of the improved efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the source format of the video frames of tagged buffer groups to append.

Pixel buffer attributes keys for the pixel buffer pool are defined in `<CoreVideo/CVPixelBuffer.h>`. To specify the pixel format type, the pixel buffer attributes dictionary should contain a value for [kCVPixelBufferPixelFormatTypeKey](../../corevideo/kcvpixelbufferpixelformattypekey.md). For example, specify a format of [kCVPixelFormatType_32BGRA](../../corevideo/kcvpixelformattype_32bgra.md) for 8-bit-per-channel BGRA. See [- appendPixelBuffer:withPresentationTime:](<../avassetwriterinputpixelbufferadaptor/append(__withpresentationtime_).md>) in [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md) for more information on choosing a pixel format.
