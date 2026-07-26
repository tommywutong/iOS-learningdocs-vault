---
title: 'isFlashAvailable(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiimagepickercontroller/isflashavailable(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/isflashavailable(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/isflashavailable%28for%3A%29.json'
content_hash: 'sha256:acfc689183bb0d38'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# isFlashAvailable(for:)

<sub>Type Method</sub>

Queries whether the specified camera has flash illumination capability.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class func isFlashAvailable(for cameraDevice: UIImagePickerController.CameraDevice) -> Bool
```

## Parameters

- `cameraDevice` — A [CameraDevice](cameradevice-swift.enum.md) constant indicating the camera whose flash capability you want to know.

## Return Value

[true](../../swift/true.md) if `cameraDevice` can use flash illumination, or [false](../../swift/false.md) if it cannot.

## See Also

### Related Documentation

- [cameraDevice](cameradevice-swift.property.md) — The camera used by the image picker controller.

### Configuring the flash behavior

- [cameraFlashMode](cameraflashmode-swift.property.md) — The flash mode used by the active camera.
- [CameraFlashMode](cameraflashmode-swift.enum.md) — Constants that specify the flash mode to use with the active camera.
