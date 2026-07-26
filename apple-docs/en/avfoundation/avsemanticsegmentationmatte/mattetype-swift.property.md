---
title: matteType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.property.json'
content_hash: 'sha256:a2a32840f4d8aefd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# matteType

<sub>Instance Property</sub>

The semantic segmentation matte image type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var matteType: AVSemanticSegmentationMatte.MatteType { get }
```

## Discussion

A semantic segmentation matte’s [matteType](mattetype-swift.property.md) is immutable for the life of the object.

## See Also

### Inspecting a segmentation matte

- [MatteType](mattetype-swift.struct.md) — A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [mattingImage](mattingimage.md) — The semantic segmentation matte’s internal image.
- [pixelFormatType](pixelformattype.md) — The pixel format type for this object’s internal matting image.
