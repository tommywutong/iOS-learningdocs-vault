---
title: startVideoCapture()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/startvideocapture()
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/startvideocapture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/startvideocapture%28%29.json'
content_hash: 'sha256:f30a91485ea265ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# startVideoCapture()

<sub>Instance Method</sub>

Starts video capture using the camera specified by the camera device property.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func startVideoCapture() -> Bool
```

## Return Value

[true](../../swift/true.md) on success or [false](../../swift/false.md) on failure. This method may return a value of [false](../../swift/false.md) for various reasons, among them the following:

- Movie capture is already in progress
- The device does not support movie capture
- The device is out of disk space

## Discussion

Use this method in conjunction with a custom overlay view to initiate the programmatic capture of a movie. You can take more than one movie without leaving the interface, but to do so requires you to hide the default image picker controls.

Calling this method while a movie is being captured has no effect. You must call the [- stopVideoCapture](<stopvideocapture().md>) method, and then wait until the associated delegate object receives an [- imagePickerController:didFinishPickingMediaWithInfo:](<../uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) message, before you can capture another movie.

Calling this method when the source type of the image picker is set to a value other than [UIImagePickerControllerSourceTypeCamera](sourcetype-swift.enum/camera.md) results in the throwing of an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) exception.

If you require additional options or more control over movie capture, use the movie capture methods in the AVFoundation framework. Refer to [AVFoundation](../../avfoundation.md).

## See Also

### Capturing still images or movies

- [- takePicture](<takepicture().md>) — Captures a still image using the camera.
- [- stopVideoCapture](<stopvideocapture().md>) — Stops video capture.
