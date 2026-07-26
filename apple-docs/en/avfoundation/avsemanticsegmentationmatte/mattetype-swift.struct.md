---
title: AVSemanticSegmentationMatte.MatteType
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.struct.json'
content_hash: 'sha256:6634bad57f04ce78'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md)

# AVSemanticSegmentationMatte.MatteType

<sub>Structure</sub>

A structure that defines the types of segmentation matte images that you can capture along with the primary image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MatteType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Matte types

- [AVSemanticSegmentationMatteTypeHair](mattetype-swift.struct/hair.md) — A matting image that segments the hair from all people in the visible field of view of an image.
- [AVSemanticSegmentationMatteTypeSkin](mattetype-swift.struct/skin.md) — A matting image that segments the skin from all people in the visible field of view of an image.
- [AVSemanticSegmentationMatteTypeTeeth](mattetype-swift.struct/teeth.md) — A matting image that segments the teeth from all people in the visible field of view of an image.
- [AVSemanticSegmentationMatteTypeGlasses](mattetype-swift.struct/glasses.md) — A matting image that segments eyeglasses and sunglasses from all people in the visible field of view of an image.

### Initializers

- [init(rawValue:)](<mattetype-swift.struct/init(rawvalue_).md>) — Creates a matte type with a string.

## See Also

### Inspecting a segmentation matte

- [matteType](mattetype-swift.property.md) — The semantic segmentation matte image type.
- [mattingImage](mattingimage.md) — The semantic segmentation matte’s internal image.
- [pixelFormatType](pixelformattype.md) — The pixel format type for this object’s internal matting image.
