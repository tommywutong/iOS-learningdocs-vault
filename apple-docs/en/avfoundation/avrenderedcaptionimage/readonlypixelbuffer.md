---
title: readOnlyPixelBuffer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avrenderedcaptionimage/readonlypixelbuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avrenderedcaptionimage/readonlypixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avrenderedcaptionimage/readonlypixelbuffer.json'
content_hash: 'sha256:988c943f7a8be5b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVRenderedCaptionImage](../avrenderedcaptionimage.md)

# readOnlyPixelBuffer

<sub>Instance Property</sub>

A CVReadOnlyPixelBuffer that contains pixel data for the rendered caption

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var readOnlyPixelBuffer: CVReadOnlyPixelBuffer { get }
```

## Discussion

The pixel format is fixed to `kCVPixelFormatType_32BGRA` defined in \<CoreVideo/CVPixelBuffer.h\>

## See Also

### Inspecting the image

- [pixelBuffer](pixelbuffer.md) — An object that contains pixel data for the rendered caption. _(deprecated)_
- [position](position.md) — A point that defines the position, in pixels, of the rendered caption image relative to the video frame.
