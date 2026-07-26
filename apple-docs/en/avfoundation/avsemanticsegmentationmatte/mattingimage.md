---
title: mattingImage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsemanticsegmentationmatte/mattingimage
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattingimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/mattingimage.json'
content_hash: 'sha256:153d1ec2377d8a11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# mattingImage

<sub>Instance Property</sub>

The semantic segmentation matte’s internal image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mattingImage: CVPixelBuffer { get }
```

## Discussion

You can determine the pixel buffer’s format type using the [pixelFormatType](pixelformattype.md) property.

## See Also

### Inspecting a segmentation matte

- [matteType](mattetype-swift.property.md) — The semantic segmentation matte image type.
- [MatteType](mattetype-swift.struct.md) — A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [pixelFormatType](pixelformattype.md) — The pixel format type for this object’s internal matting image.
