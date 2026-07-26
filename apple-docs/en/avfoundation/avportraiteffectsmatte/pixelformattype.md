---
title: pixelFormatType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avportraiteffectsmatte/pixelformattype
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/pixelformattype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/pixelformattype.json'
content_hash: 'sha256:8705cf069a7afbd4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# pixelFormatType

<sub>Instance Property</sub>

The pixel format type of this portrait effects matte’s internal image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var pixelFormatType: OSType { get }
```

## Discussion

The only supported pixel format type for the matting image is [kCVPixelFormatType_OneComponent8](../../corevideo/kcvpixelformattype_onecomponent8.md).

## See Also

### Examining a Portrait Effects matte

- [Extracting Portrait Effects matte image data from a photo](../extracting-portrait-effects-matte-image-data-from-a-photo.md) — Check for portrait effects matte metadata in existing images.
- [mattingImage](mattingimage.md) — The portrait effects matte’s internal image, formatted as a pixel buffer.
- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — A dictionary of primitive map information used for writing an image file with a portrait effects matte.
