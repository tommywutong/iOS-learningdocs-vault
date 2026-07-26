---
title: 'isCameraDeviceAvailable(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontroller/iscameradeviceavailable(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/iscameradeviceavailable(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/iscameradeviceavailable%28_%3A%29.json'
content_hash: 'sha256:737526213a145886'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# isCameraDeviceAvailable(_:)

<sub>Type Method</sub>

Queries whether the specified camera is available.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func isCameraDeviceAvailable(_ cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

## Parameters

- `cameraDevice` — A [CameraDevice](cameradevice-swift.enum.md) constant indicating the camera whose availability you want to check.

## Return Value

[true](../../swift/true.md) if the camera indicated by `cameraDevice` is available, or [false](../../swift/false.md) if it is not available.

## See Also

### Related Documentation

- [+ isFlashAvailableForCameraDevice:](<isflashavailable(for_).md>) — Queries whether the specified camera has flash illumination capability.
- [+ availableCaptureModesForCameraDevice:](<availablecapturemodes(for_).md>) — Retrieves the capture modes supported by the specified camera device.

### Configuring the camera to use

- [cameraDevice](cameradevice-swift.property.md) — The camera used by the image picker controller.
- [CameraDevice](cameradevice-swift.enum.md) — Constants that specify the camera to use for image or movie capture.
