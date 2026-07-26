---
title: livePhoto
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/infokey/livephoto
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey/livephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey/livephoto.json'
content_hash: 'sha256:bfc38de867f48e06'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [InfoKey](../infokey.md)

# livePhoto

<sub>Type Property</sub>

The Live Photo representation of the selected or captured photo.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static let livePhoto: UIImagePickerController.InfoKey
```

## Discussion

A Live Photo is a picture, that includes motion and sound from the moments just before and after its capture. On compatible devices, the Camera app captures all photos as Live Photos by default, but the [imagePickerController:didFinishPickingImage:editingInfo:](../../uiimagepickercontrollerdelegate/imagepickercontroller_didfinishpickingimage_editinginfo_.md) method’s `image` parameter contains only the still image representation.

To obtain the motion and sound content of a live photo for display (using the [PHLivePhotoView](../../../photosui/phlivephotoview.md) class), include the `kUTTypeImage` and `kUTTypeLivePhoto` identifiers in the allowed media types when configuring an image picker controller. When the user picks or captures a Live Photo, the `editingInfo` dictionary contains the [UIImagePickerControllerLivePhoto](livephoto.md) key, with a [PHLivePhoto](../../../photos/phlivephoto.md) representation of the photo as the corresponding value.

## See Also

### Constants

- [UIImagePickerControllerCropRect](croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](imageurl.md) — The URL of the image file.
- [UIImagePickerControllerMediaMetadata](mediametadata.md) — Metadata for a newly-captured photograph.
- [UIImagePickerControllerMediaType](mediatype.md) — The media type selected by the user.
- [UIImagePickerControllerMediaURL](mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerOriginalImage](originalimage.md) — The original, uncropped image selected by the user.
- [UIImagePickerControllerPHAsset](phasset.md) — A Photos asset for the image. _(deprecated)_
- [UIImagePickerControllerReferenceURL](referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_
