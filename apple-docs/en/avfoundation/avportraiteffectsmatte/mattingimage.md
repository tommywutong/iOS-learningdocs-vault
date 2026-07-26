---
title: mattingImage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avportraiteffectsmatte/mattingimage
source_url: 'https://developer.apple.com/documentation/avfoundation/avportraiteffectsmatte/mattingimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avportraiteffectsmatte/mattingimage.json'
content_hash: 'sha256:1137382a7bba766a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPortraitEffectsMatte](../avportraiteffectsmatte.md)

# mattingImage

<sub>Instance Property</sub>

The portrait effects matte’s internal image, formatted as a pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var mattingImage: CVPixelBuffer { get }
```

## Discussion

Query the pixel format using the [pixelFormatType](pixelformattype.md) property.

## See Also

### Examining a Portrait Effects matte

- [Extracting Portrait Effects matte image data from a photo](../extracting-portrait-effects-matte-image-data-from-a-photo.md) — Check for portrait effects matte metadata in existing images.
- [pixelFormatType](pixelformattype.md) — The pixel format type of this portrait effects matte’s internal image.
- [- dictionaryRepresentationForAuxiliaryDataType:](<dictionaryrepresentation(forauxiliarydatatype_).md>) — A dictionary of primitive map information used for writing an image file with a portrait effects matte.
