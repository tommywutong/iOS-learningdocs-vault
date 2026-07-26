---
title: mediaType
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/mediatype
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/mediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/mediatype.json'
content_hash: 'sha256:cdb7070b7ab4c553'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# mediaType

<sub>Type Property</sub>

The media type selected by the user.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let mediaType: UIImagePickerController.InfoKey
```

## Discussion

The value for this key is an [NSString](../../../foundation/nsstring.md) object containing a type code such as `kUTTypeImage` or `kUTTypeMovie`.

## See Also

### Constants

- [UIImagePickerControllerCropRect](croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](imageurl.md) — The URL of the image file.
- [UIImagePickerControllerLivePhoto](livephoto.md) — The Live Photo representation of the selected or captured photo.
- [UIImagePickerControllerMediaMetadata](mediametadata.md) — Metadata for a newly-captured photograph.
- [UIImagePickerControllerMediaURL](mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerOriginalImage](originalimage.md) — The original, uncropped image selected by the user.
- [UIImagePickerControllerPHAsset](phasset.md) — A Photos asset for the image. _(deprecated)_
- [UIImagePickerControllerReferenceURL](referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_
