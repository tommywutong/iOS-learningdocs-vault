---
title: 'init(assetWriterInput:sourcePixelBufferAttributes:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/init(assetwriterinput:sourcepixelbufferattributes:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/init(assetwriterinput:sourcepixelbufferattributes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/init%28assetwriterinput%3Asourcepixelbufferattributes%3A%29.json'
content_hash: 'sha256:411b7da3c2309b2b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md)

# init(assetWriterInput:sourcePixelBufferAttributes:)

<sub>Initializer</sub>

Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file.

> [!warning] Deprecated
> Use AVAssetWriter.inputPixelBufferReceiver(for:pixelBufferAttributes:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(assetWriterInput input: AVAssetWriterInput, sourcePixelBufferAttributes: [String : Any]? = nil)
```

## Parameters

- `input` — An asset writer input that accepts [AVMediaTypeVideo](../avmediatype/video.md) as its media type. The system raises an error if you specify an input that’s already connected to a pixel buffer adaptor.

- `sourcePixelBufferAttributes` — A dictionary that describes the attributes of pixel buffers that the input’s pixel buffer pool vends. If your app doesn’t need a pixel buffer pool for allocating buffers, set this value to `nil`.

## Discussion

To take advantage of the efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the format of the buffers you append.
