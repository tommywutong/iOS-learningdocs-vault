---
title: cameraFlashMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.property.json'
content_hash: 'sha256:9b3a7a0f2dbab3af'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# cameraFlashMode

<sub>Instance Property</sub>

The flash mode used by the active camera.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cameraFlashMode: UIImagePickerController.CameraFlashMode { get set }
```

## Discussion

The various flash modes are listed in the [CameraFlashMode](cameraflashmode-swift.enum.md) enumeration. The default value is [UIImagePickerControllerCameraFlashModeAuto](cameraflashmode-swift.enum/auto.md).

The value of this property specifies the behavior of the still-image flash when the value of the [cameraCaptureMode](cameracapturemode-swift.property.md) property is [UIImagePickerControllerCameraCaptureModePhoto](cameracapturemode-swift.enum/photo.md), and specifies the behavior of the video torch when [cameraCaptureMode](cameracapturemode-swift.property.md) is [UIImagePickerControllerCameraCaptureModeVideo](cameracapturemode-swift.enum/video.md).

## See Also

### Related Documentation

- [cameraDevice](cameradevice-swift.property.md) — The camera used by the image picker controller.
- [cameraCaptureMode](cameracapturemode-swift.property.md) — The capture mode used by the camera.

### Configuring the flash behavior

- [+ isFlashAvailableForCameraDevice:](<isflashavailable(for_).md>) — Queries whether the specified camera has flash illumination capability.
- [CameraFlashMode](cameraflashmode-swift.enum.md) — Constants that specify the flash mode to use with the active camera.
