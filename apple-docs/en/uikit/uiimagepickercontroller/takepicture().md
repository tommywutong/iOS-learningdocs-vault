---
title: takePicture()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.1+, iPadOS 3.1+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/takepicture()
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/takepicture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/takepicture%28%29.json'
content_hash: 'sha256:a8ed5bf69b798364'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# takePicture()

<sub>Instance Method</sub>

Captures a still image using the camera.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func takePicture()
```

## Discussion

Use this method in conjunction with a custom overlay view to initiate the programmatic capture of a still image. This supports taking more than one picture without leaving the interface, but requires that you hide the default image picker controls.

Calling this method while an image is being captured has no effect. You must wait until the associated delegate object receives an [- imagePickerController:didFinishPickingMediaWithInfo:](<../uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) message before you can capture another picture.

Calling this method when the source type of the image picker is set to a value other than [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md) results in the throwing of an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

## See Also

### Related Documentation

- [cameraOverlayView](cameraoverlayview.md) — The view to display on top of the default image picker interface.

### Capturing still images or movies

- [- startVideoCapture](<startvideocapture().md>) — Starts video capture using the camera specified by the camera device property.
- [- stopVideoCapture](<stopvideocapture().md>) — Stops video capture.
