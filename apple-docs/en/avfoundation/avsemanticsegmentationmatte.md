---
title: AVSemanticSegmentationMatte
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsemanticsegmentationmatte
source_url: 'https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsemanticsegmentationmatte.json'
content_hash: 'sha256:f7726b22491c293f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSemanticSegmentationMatte

<sub>Class</sub>

An object that wraps a matting image for a particular semantic segmentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSemanticSegmentationMatte
```

## Overview

The matting image stores its pixel data as [CVPixelBuffer](../corevideo/cvpixelbuffer-q2e.md) objects in [kCVPixelFormatType_OneComponent8](../corevideo/kcvpixelformattype_onecomponent8.md) format. The image file contains the semantic segmentation matte as an auxiliary image, accessible using the ImageIO framework’s [CGImageSourceCopyAuxiliaryDataInfoAtIndex(_:_:_:)](<../imageio/cgimagesourcecopyauxiliarydatainfoatindex(______).md>) function.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a segmentation matte

- [+ semanticSegmentationMatteFromImageSourceAuxiliaryDataType:dictionaryRepresentation:error:](<avsemanticsegmentationmatte/init(fromimagesourceauxiliarydatatype_dictionaryrepresentation_).md>) — Returns a new semantic segmentation matte instance from auxiliary image information in an image file.
- [- semanticSegmentationMatteByReplacingSemanticSegmentationMatteWithPixelBuffer:error:](<avsemanticsegmentationmatte/replacingsemanticsegmentationmatte(with_).md>) — Returns a semantic segmentation matte instance that wraps the replacement pixel buffer.
- [- semanticSegmentationMatteByApplyingExifOrientation:](<avsemanticsegmentationmatte/applyingexiforientation(__).md>) — Returns a new semantic segmentation matte instance with the specified Exif orientation applied.
- [- dictionaryRepresentationForAuxiliaryDataType:](<avsemanticsegmentationmatte/dictionaryrepresentation(forauxiliarydatatype_).md>) — Returns a dictionary of primitive map information to use when writing an image file with a semantic segmentation matte.

### Inspecting a segmentation matte

- [matteType](avsemanticsegmentationmatte/mattetype-swift.property.md) — The semantic segmentation matte image type.
- [MatteType](avsemanticsegmentationmatte/mattetype-swift.struct.md) — A structure that defines the types of segmentation matte images that you can capture along with the primary image.
- [mattingImage](avsemanticsegmentationmatte/mattingimage.md) — The semantic segmentation matte’s internal image.
- [pixelFormatType](avsemanticsegmentationmatte/pixelformattype.md) — The pixel format type for this object’s internal matting image.

## See Also

### Matte data

- [AVPortraitEffectsMatte](avportraiteffectsmatte.md) — An auxiliary image used to separate foreground from background with high resolution.
