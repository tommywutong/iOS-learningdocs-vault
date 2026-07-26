---
title: pixelBuffer
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/pixelbuffer
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/pixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/pixelbuffer.json'
content_hash: 'sha256:20059a54d71d1e17'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# pixelBuffer

<sub>Instance Property</sub>

The CoreVideo pixel buffer this image was created from, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## Discussion

If this image was create using the [- initWithCVPixelBuffer:](<init(cvpixelbuffer_)-3wng7.md>) initializer, this property’s value is the [CVPixelBuffer](../../corevideo/cvpixelbuffer.md) object that provides the image’s underlying image data. Do not modify the contents of this pixel buffer; doing so will cause undefined rendering results.

Otherwise, this property’s value is `nil`—in this case you can obtain a pixel buffer by rendering the image with the [CIContext](../cicontext.md) [- render:toCVPixelBuffer:](<../cicontext/render(__to_).md>) method.

## See Also

### Accessing Original Image Content

- [CGImage](cgimage.md) — The CoreGraphics image object this image was created from, if applicable.
- [depthData](depthdata.md) — Depth data associated with the image.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte associated with the image.
- [semanticSegmentationMatte](semanticsegmentationmatte.md)
