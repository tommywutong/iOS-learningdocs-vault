---
title: mediaMetadata
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/mediametadata
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/mediametadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/mediametadata.json'
content_hash: 'sha256:ecbb4c4052cf1269'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# mediaMetadata

<sub>Type Property</sub>

Metadata for a newly-captured photograph.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let mediaMetadata: UIImagePickerController.InfoKey
```

## Discussion

This key is valid only when using an image picker whose source type is set to [UIImagePickerControllerSourceTypeCamera](../sourcetype-swift.enum/camera.md), and applies only to still images.

The value for this key is an [NSDictionary](../../../foundation/nsdictionary.md) object that contains the metadata of the photo that was just captured. To store the metadata along with the image in the Camera Roll, use the [PHAssetChangeRequest](../../../photos/phassetchangerequest.md) class from the Photos framework.

## See Also

### Constants

- [UIImagePickerControllerCropRect](croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](imageurl.md) — The URL of the image file.
- [UIImagePickerControllerLivePhoto](livephoto.md) — The Live Photo representation of the selected or captured photo.
- [UIImagePickerControllerMediaType](mediatype.md) — The media type selected by the user.
- [UIImagePickerControllerMediaURL](mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerOriginalImage](originalimage.md) — The original, uncropped image selected by the user.
- [UIImagePickerControllerPHAsset](phasset.md) — A Photos asset for the image. _(deprecated)_
- [UIImagePickerControllerReferenceURL](referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_
