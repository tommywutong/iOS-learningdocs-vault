---
title: UIImagePickerControllerDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontrollerdelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontrollerdelegate.json'
content_hash: 'sha256:2e968acbe22cf4ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIImagePickerControllerDelegate

<sub>Protocol</sub>

A set of methods that your delegate object must implement to interact with the image picker interface.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor protocol UIImagePickerControllerDelegate : NSObjectProtocol
```

## Overview

The methods of this protocol notify your delegate when the user either picks an image or movie, or cancels the picker operation. The delegate methods are responsible for dismissing the picker when the operation completes. To dismiss the picker, call the [- dismissViewControllerAnimated:completion:](<uiviewcontroller/dismiss(animated_completion_).md>) method of the parent controller responsible for displaying the [UIImagePickerController](uiimagepickercontroller.md) object.

To save a still image to the user’s Camera Roll album, call the [UIImageWriteToSavedPhotosAlbum](<uiimagewritetosavedphotosalbum(________).md>) function from within the body of the [- imagePickerController:didFinishPickingMediaWithInfo:](<uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) method. To save a movie to the user’s Camera Roll album, instead call the [UISaveVideoAtPathToSavedPhotosAlbum](<uisavevideoatpathtosavedphotosalbum(________).md>) function. These functions, described in `UIKit Functions`, save the image or movie only; they don’t save metadata.

To write additional metadata when saving an image to the Camera Roll, use the [PHAssetChangeRequest](../photos/phassetchangerequest.md) class from the Photos framework. See the description for the [UIImagePickerControllerMediaMetadata](uiimagepickercontroller/infokey/mediametadata.md) key.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Closing the picker

- [- imagePickerController:didFinishPickingMediaWithInfo:](<uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) — Tells the delegate that the user picked a still image or movie.
- [- imagePickerControllerDidCancel:](<uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(__).md>) — Tells the delegate that the user canceled the pick operation.

### Getting the editing information

- [InfoKey](uiimagepickercontroller/infokey.md) — Keys you use to retrieve information from the editing dictionary about the media that the user selected.

## See Also

### Responding to interactions with the picker

- [delegate](uiimagepickercontroller/delegate.md) — The image picker’s delegate object.
