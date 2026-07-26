---
title: displaySizeImage
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/displaysizeimage
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/displaysizeimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/displaysizeimage.json'
content_hash: 'sha256:de78048d9a139bcc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# displaySizeImage

<sub>Instance Property</sub>

An image of the asset’s contents, appropriately sized for display.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var displaySizeImage: UIImage? { get }
```

<sub>macOS</sub>

```swift
var displaySizeImage: NSImage? { get }
```

## Discussion

This property does not provide the full-sized image for a photo asset but rather a scaled-down image appropriate for use in a photo editing user interface. To load the full-sized asset image, use the [fullSizeImageURL](fullsizeimageurl.md) property.

## See Also

### Working with Photo Assets

- [fullSizeImageOrientation](fullsizeimageorientation.md) — The Exif display orientation of the full-size image file.
- [fullSizeImageURL](fullsizeimageurl.md) — The URL to a file that contains the full-sized image data.
