---
title: cameraDevice
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameradevice-swift.property
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameradevice-swift.property.json'
content_hash: 'sha256:083ce04445f66df2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# cameraDevice

<sub>Instance Property</sub>

The camera used by the image picker controller.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var cameraDevice: UIImagePickerController.CameraDevice { get set }
```

## Discussion

The default is [UIImagePickerControllerCameraDeviceRear](cameradevice-swift.enum/rear.md).

## See Also

### Related Documentation

- [+ isFlashAvailableForCameraDevice:](<isflashavailable(for_).md>) — Queries whether the specified camera has flash illumination capability.
- [+ availableCaptureModesForCameraDevice:](<availablecapturemodes(for_).md>) — Retrieves the capture modes supported by the specified camera device.

### Configuring the camera to use

- [+ isCameraDeviceAvailable:](<iscameradeviceavailable(__).md>) — Queries whether the specified camera is available.
- [CameraDevice](cameradevice-swift.enum.md) — Constants that specify the camera to use for image or movie capture.
