---
title: 'assetWriterInputPixelBufferAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/assetwriterinputpixelbufferadaptorwithassetwriterinput:sourcepixelbufferattributes:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/assetwriterinputpixelbufferadaptorwithassetwriterinput:sourcepixelbufferattributes:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinputpixelbufferadaptor/assetwriterinputpixelbufferadaptorwithassetwriterinput%3Asourcepixelbufferattributes%3A.json'
content_hash: 'sha256:b64ac0cdc462afb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInputPixelBufferAdaptor](../avassetwriterinputpixelbufferadaptor.md)

# assetWriterInputPixelBufferAdaptorWithAssetWriterInput:sourcePixelBufferAttributes:

<sub>Type Method</sub>

Returns a new pixel buffer adaptor that appends pixel buffers to write to the output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) assetWriterInputPixelBufferAdaptorWithAssetWriterInput:(AVAssetWriterInput *) input sourcePixelBufferAttributes:(NSDictionary<NSString *,id> *) sourcePixelBufferAttributes;
```

## Parameters

- `input` — An asset writer input that accepts [AVMediaTypeVideo](../avmediatype/video.md) as its media type. The system raises an error if you specify an input that’s already connected to a pixel buffer adaptor.

- `sourcePixelBufferAttributes` — A dictionary that describes the attributes of pixel buffers that the input’s pixel buffer pool vends. If your app doesn’t need a pixel buffer pool for allocating buffers, set this value to `nil`.

## Return Value

A new pixel buffer adaptor to receive pixel buffers for writing to the output file.

## Discussion

To take advantage of the efficiency of appending buffers created from the adaptor’s pixel buffer pool, specify pixel buffer attributes that most closely accommodate the format of the buffers you append.

## See Also

### Creating an adaptor

- [- initWithAssetWriterInput:sourcePixelBufferAttributes:](<init(assetwriterinput_sourcepixelbufferattributes_).md>) — Creates a new pixel buffer adaptor to receive pixel buffers for writing to the output file. _(deprecated)_
