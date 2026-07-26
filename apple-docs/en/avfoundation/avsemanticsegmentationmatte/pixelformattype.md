---
title: pixelFormatType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsemanticsegmentationmatte/pixelformattype
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/pixelformattype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/pixelformattype.json'
content_hash: 'sha256:fbeaddd75a405356'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# pixelFormatType

<sub>Instance Property</sub>

The pixel format type for this object’s internal matting image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pixelFormatType: OSType { get }
```

## Discussion

Currently, the only supported pixel format type for the matting image is [kCVPixelFormatType_OneComponent8](../../corevideo/kcvpixelformattype_onecomponent8.md).

## See Also

### Inspecting a segmentation matte

- [matteType](mattetype-swift.property.md) — The semantic segmentation matte image type.
- [MatteType](mattetype-swift.struct.md) — A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [mattingImage](mattingimage.md) — The semantic segmentation matte’s internal image.
