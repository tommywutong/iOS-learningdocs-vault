---
title: 'imagePickerControllerDidCancel(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontrollerdelegate/imagepickercontrollerdidcancel%28_%3A%29.json'
content_hash: 'sha256:4ca74deb297d93d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerControllerDelegate](../uiimagepickercontrollerdelegate.md)

# imagePickerControllerDidCancel(_:)

<sub>Instance Method</sub>

Tells the delegate that the user canceled the pick operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func imagePickerControllerDidCancel(_ picker: UIImagePickerController)
```

## Parameters

- `picker` — The controller object managing the image picker interface.

## Discussion

Your delegate’s implementation of this method should dismiss the picker view by calling the [- dismissViewControllerAnimated:completion:](<../uiviewcontroller/dismiss(animated_completion_).md>) method of the parent view controller.

Implementation of this method is optional, but expected.

## See Also

### Closing the picker

- [- imagePickerController:didFinishPickingMediaWithInfo:](<imagepickercontroller(__didfinishpickingmediawithinfo_).md>) — Tells the delegate that the user picked a still image or movie.
