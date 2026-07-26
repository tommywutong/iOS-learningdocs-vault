---
title: recommendedPixelBufferAttributes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 17.4+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb.json'
content_hash: 'sha256:b732fd9530d9bfb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# recommendedPixelBufferAttributes

<sub>Instance Property</sub>

Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelbuffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var recommendedPixelBufferAttributes: CVPixelBufferAttributes { get }
```

## Discussion

The returned attributes are not sufficient for pixel buffer creation. Use `CVPixelBufferAttributes/init?(merging:)` to merge these with other required attributes.

## See Also

### Accessing the pixel buffer

- [- copyDisplayedPixelBuffer](<displayedpixelbuffer().md>)
