---
title: cgImage
framework: Core Image
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coreimage/ciimage/cgimage
source_url: 'https://developer.apple.com/documentation/coreimage/ciimage/cgimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/ciimage/cgimage.json'
content_hash: 'sha256:b35afbbd4fd85527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIImage](../ciimage.md)

# cgImage

<sub>Instance Property</sub>

The CoreGraphics image object this image was created from, if applicable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cgImage: CGImage? { get }
```

## Discussion

If this image was created using the [- initWithCGImage:](<init(cgimage_)-2kvvb.md>) or [- initWithContentsOfURL:](<init(contentsof_).md>) initializer, this property’s value is the [CGImage](../../coregraphics/cgimage.md) object that provides the image’s underlying image data. Otherwise, this property’s value is `nil`—in this case you can obtain a CoreGraphics image by rendering the image with the [CIContext](../cicontext.md) [- createCGImage:fromRect:](<../cicontext/createcgimage(__from_).md>) method.

## See Also

### Accessing Original Image Content

- [pixelBuffer](pixelbuffer.md) — The CoreVideo pixel buffer this image was created from, if applicable.
- [depthData](depthdata.md) — Depth data associated with the image.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte associated with the image.
- [semanticSegmentationMatte](semanticsegmentationmatte.md)
