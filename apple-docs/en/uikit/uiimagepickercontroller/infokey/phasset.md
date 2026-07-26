---
title: phAsset
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/phasset
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/phasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/phasset.json'
content_hash: 'sha256:6abdd3ffdb7923c3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# phAsset

<sub>Type Property</sub>

A Photos asset for the image.

> [!warning] Deprecated
> Use [PHPickerViewController](../../../photosui/phpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let phAsset: UIImagePickerController.InfoKey
```

## Discussion

The value of this key is a [PHAsset](../../../photos/phasset.md) object.

## See Also

### Constants

- [UIImagePickerControllerCropRect](croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](imageurl.md) — The URL of the image file.
- [UIImagePickerControllerLivePhoto](livephoto.md) — The Live Photo representation of the selected or captured photo.
- [UIImagePickerControllerMediaMetadata](mediametadata.md) — Metadata for a newly-captured photograph.
- [UIImagePickerControllerMediaType](mediatype.md) — The media type selected by the user.
- [UIImagePickerControllerMediaURL](mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerOriginalImage](originalimage.md) — The original, uncropped image selected by the user.
- [UIImagePickerControllerReferenceURL](referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_
