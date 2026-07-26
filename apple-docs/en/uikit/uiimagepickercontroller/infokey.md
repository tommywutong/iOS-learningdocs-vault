---
title: UIImagePickerController.InfoKey
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/infokey
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/infokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/infokey.json'
content_hash: 'sha256:370ed67eb8e1045b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.InfoKey

<sub>Structure</sub>

Keys you use to retrieve information from the editing dictionary about the media that the user selected.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct InfoKey
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerCropRect](infokey/croprect.md) — The cropping rectangle that was applied to the original image.
- [UIImagePickerControllerEditedImage](infokey/editedimage.md) — An image edited by the user.
- [UIImagePickerControllerImageURL](infokey/imageurl.md) — The URL of the image file.
- [UIImagePickerControllerLivePhoto](infokey/livephoto.md) — The Live Photo representation of the selected or captured photo.
- [UIImagePickerControllerMediaMetadata](infokey/mediametadata.md) — Metadata for a newly-captured photograph.
- [UIImagePickerControllerMediaType](infokey/mediatype.md) — The media type selected by the user.
- [UIImagePickerControllerMediaURL](infokey/mediaurl.md) — The filesystem URL for the movie.
- [UIImagePickerControllerOriginalImage](infokey/originalimage.md) — The original, uncropped image selected by the user.
- [UIImagePickerControllerPHAsset](infokey/phasset.md) — A Photos asset for the image. _(deprecated)_
- [UIImagePickerControllerReferenceURL](infokey/referenceurl.md) — The Assets Library URL for the original version of the picked item. _(deprecated)_

### Initializers

- [init(rawValue:)](<infokey/init(rawvalue_).md>) — Creates a new editing information key with the specified raw value.
