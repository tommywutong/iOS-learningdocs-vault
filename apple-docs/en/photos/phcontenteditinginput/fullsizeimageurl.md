---
title: fullSizeImageURL
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcontenteditinginput/fullsizeimageurl
source_url: 'https://developer.apple.com/documentation/photos/phcontenteditinginput/fullsizeimageurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcontenteditinginput/fullsizeimageurl.json'
content_hash: 'sha256:237682bf6eeece7f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHContentEditingInput](../phcontenteditinginput.md)

# fullSizeImageURL

<sub>Instance Property</sub>

The URL to a file that contains the full-sized image data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var fullSizeImageURL: URL? { get }
```

## Discussion

Typically, your app or extension does not need to load a full-sized image for use in an editing UI. Instead, use the [displaySizeImage](displaysizeimage.md) property to retrieve an image suitable for screen display. You can then load the full-sized image on a background queue so that it will be ready by the time the user finishes editing the display-size image. At that time, apply the user’s adjustments to the full-sized image and then use the [PHContentEditingOutput](../phcontenteditingoutput.md) class to commit the edit to the photo library.

## See Also

### Working with Photo Assets

- [displaySizeImage](displaysizeimage.md) — An image of the asset’s contents, appropriately sized for display.
- [fullSizeImageOrientation](fullsizeimageorientation.md) — The Exif display orientation of the full-size image file.
