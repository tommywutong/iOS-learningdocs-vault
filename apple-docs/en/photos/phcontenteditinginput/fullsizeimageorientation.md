---
title: fullSizeImageOrientation
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/fullsizeimageorientation
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/fullsizeimageorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/fullsizeimageorientation.json'
content_hash: 'sha256:1d1a13b0962125dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# fullSizeImageOrientation

<sub>Instance Property</sub>

The Exif display orientation of the full-size image file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fullSizeImageOrientation: Int32 { get }
```

## Discussion

This property’s value is a raw numeric value describing the encoded image orientation according to the TIFF and Exif specifications. To more easily work with such values, convert this value to the [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md) type.

## See Also

### Related Documentation

- [CGImagePropertyOrientation](../../imageio/cgimagepropertyorientation.md) — A value describing the intended display orientation for an image.

### Working with Photo Assets

- [displaySizeImage](displaysizeimage.md) — An image of the asset’s contents, appropriately sized for display.
- [fullSizeImageURL](fullsizeimageurl.md) — The URL to a file that contains the full-sized image data.
