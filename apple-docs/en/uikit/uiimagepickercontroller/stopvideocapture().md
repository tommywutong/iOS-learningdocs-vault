---
title: stopVideoCapture()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/stopvideocapture()
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/stopvideocapture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/stopvideocapture%28%29.json'
content_hash: 'sha256:a2048068c66e83fd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# stopVideoCapture()

<sub>Instance Method</sub>

Stops video capture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func stopVideoCapture()
```

## Discussion

After you call this method to stop video capture, the system calls the image picker delegate’s [- imagePickerController:didFinishPickingMediaWithInfo:](<../uiimagepickercontrollerdelegate/imagepickercontroller(__didfinishpickingmediawithinfo_).md>) method.

## See Also

### Capturing still images or movies

- [- takePicture](<takepicture().md>) — Captures a still image using the camera.
- [- startVideoCapture](<startvideocapture().md>) — Starts video capture using the camera specified by the camera device property.
