---
title: 'availableCaptureModes(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontroller/availablecapturemodes(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/availablecapturemodes(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/availablecapturemodes%28for%3A%29.json'
content_hash: 'sha256:071d158390dfe289'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# availableCaptureModes(for:)

<sub>Type Method</sub>

Retrieves the capture modes supported by the specified camera device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func availableCaptureModes(for cameraDevice: UIImagePickerController.CameraDevice) -> [NSNumber]?
```

## Parameters

- `cameraDevice` — A [CameraDevice](cameradevice-swift.enum.md) constant indicating the camera you want to interrogate.

## Return Value

An array of [NSNumber](../../foundation/nsnumber.md) objects indicating the capture modes supported by `cameraDevice`.

## Discussion

See [CameraCaptureMode](cameracapturemode-swift.enum.md) for possible values.

## See Also

### Configuring the camera capture mode

- [cameraCaptureMode](cameracapturemode-swift.property.md) — The capture mode used by the camera.
- [CameraCaptureMode](cameracapturemode-swift.enum.md) — Constants that specify the category of media for the camera to capture.
