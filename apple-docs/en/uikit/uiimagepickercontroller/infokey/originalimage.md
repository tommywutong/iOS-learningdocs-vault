---
title: originalImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/originalimage
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/originalimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/originalimage.json'
content_hash: 'sha256:8e69c6dcc2d65d0f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# originalImage

<sub>Type Property</sub>

The original, uncropped image selected by the user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let originalImage: UIImagePickerController.InfoKey
```

## Discussion

The value for this key is a [UIImage](../../uiimage.md) object.

## See Also

### Constants

- [UIImagePickerControllerCropRect](croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](imageurl.md) — The URL of the image file.
- [UIImagePickerControllerLivePhoto](livephoto.md) — The Live Photo representation of the selected or captured photo.
- [UIImagePickerControllerMediaMetadata](mediametadata.md) — Metadata for a newly-captured photograph.
- [UIImagePickerControllerMediaType](mediatype.md) — The media type selected by the user.
- [UIImagePickerControllerMediaURL](mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerPHAsset](phasset.md) — A Photos asset for the image. _(deprecated)_
- [UIImagePickerControllerReferenceURL](referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_
