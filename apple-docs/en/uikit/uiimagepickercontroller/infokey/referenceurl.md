---
title: referenceURL
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.1+（11.0 起废弃）, iPadOS 4.1+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/referenceurl
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/referenceurl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/referenceurl.json'
content_hash: 'sha256:6c91c2e6db5f7104'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# referenceURL

<sub>Type Property</sub>

The Assets Library URL for the original version of the picked item.

> [!warning] Deprecated
> Use [PHPickerViewController](../../../photosui/phpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
static let referenceURL: UIImagePickerController.InfoKey
```

## Discussion

After the user edits a picked item—such as by cropping an image or trimming a movie—the URL continues to point to the original version of the picked item.

The value for this key is an [NSURL](../../../foundation/nsurl.md) object.

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
- [UIImagePickerControllerPHAsset](phasset.md) — A Photos asset for the image. _(deprecated)_
