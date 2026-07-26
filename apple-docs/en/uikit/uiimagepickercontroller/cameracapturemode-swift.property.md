---
title: cameraCaptureMode
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.property.json'
content_hash: 'sha256:edc9c0464dab6308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# cameraCaptureMode

<sub>Instance Property</sub>

The capture mode used by the camera.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cameraCaptureMode: UIImagePickerController.CameraCaptureMode { get set }
```

## Discussion

The various capture modes are listed in the [CameraCaptureMode](cameracapturemode-swift.enum.md) enumeration. The default value is [UIImagePickerControllerCameraCaptureModePhoto](cameracapturemode-swift.enum/photo.md).

## See Also

### Related Documentation

- [cameraDevice](cameradevice-swift.property.md) — The camera used by the image picker controller.

### Configuring the camera capture mode

- [+ availableCaptureModesForCameraDevice:](<availablecapturemodes(for_).md>) — Retrieves the capture modes supported by the specified camera device.
- [CameraCaptureMode](cameracapturemode-swift.enum.md) — Constants that specify the category of media for the camera to capture.
