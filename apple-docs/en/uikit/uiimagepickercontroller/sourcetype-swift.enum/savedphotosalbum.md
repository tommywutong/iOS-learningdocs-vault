---
title: UIImagePickerController.SourceType.savedPhotosAlbum
framework: UIKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+（27.0 起废弃）, iPadOS 2.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/sourcetype-swift.enum/savedphotosalbum.json'
content_hash: 'sha256:3f674ab91247f5a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIImagePickerController](../../uiimagepickercontroller.md) · [SourceType](../sourcetype-swift.enum.md)

# UIImagePickerController.SourceType.savedPhotosAlbum

<sub>Case</sub>

Specifies the device’s Camera Roll album as the source for the image picker controller.

> [!warning] Deprecated
> Use [PHPickerViewController](../../../photosui/phpickerviewcontroller.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case savedPhotosAlbum
```

## Discussion

If the device does not have a camera, specifies the Saved Photos album as the source.

## See Also

### Constants

- [UIImagePickerControllerSourceTypeCamera](camera.md) — Specifies the device’s built-in camera as the source for the image picker controller.
- [UIImagePickerControllerSourceTypePhotoLibrary](photolibrary.md) — Specifies the device’s photo library as the source for the image picker controller. _(deprecated)_
