---
title: sourceImage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（27.0 起废弃）, iPadOS 9.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avasynchronousciimagefilteringrequest/sourceimage
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousciimagefilteringrequest/sourceimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousciimagefilteringrequest/sourceimage.json'
content_hash: 'sha256:7575e7631926825e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAsynchronousCIImageFilteringRequest](../avasynchronousciimagefilteringrequest.md)

# sourceImage

<sub>Instance Property</sub>

The current video frame image.

> [!warning] Deprecated
> Use AVCIImageFilteringParameters instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sourceImage: CIImage { get }
```

## Discussion

To apply a Core Image filter to this image, assign it to the `inputImage` parameter of a [CIFilter](../../coreimage/cifilter-swift.class.md) object, or use a [CIImage](../../coreimage/ciimage.md) convenience method such as the [applyingFilter(_:parameters:)](<../../coreimage/ciimage/applyingfilter(__parameters_).md>) method.

The pixel format for this image is the [BGRA8](../../coreimage/ciformat/bgra8.md) format (of the [kCVPixelFormatType_32BGRA](../../corevideo/kcvpixelformattype_32bgra.md) type). Unlike when processing video with the [AVAsynchronousVideoCompositionRequest](../avasynchronousvideocompositionrequest.md) class, the [renderContext](../avasynchronousvideocompositionrequest/rendercontext.md) object’s [renderTransform](../avvideocompositionrendercontext/rendertransform.md) property is already applied to this image.
