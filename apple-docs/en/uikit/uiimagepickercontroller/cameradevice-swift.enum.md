---
title: UIImagePickerController.CameraDevice
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameradevice-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameradevice-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameradevice-swift.enum.json'
content_hash: 'sha256:0bc9b74fa5517d16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.CameraDevice

<sub>Enumeration</sub>

Constants that specify the camera to use for image or movie capture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum CameraDevice
```

## Overview

The constants in this enumeration are for use as values of the [cameraDevice](cameradevice-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerCameraDeviceRear](cameradevice-swift.enum/rear.md) — Specifies the camera on the rear of the device.
- [UIImagePickerControllerCameraDeviceFront](cameradevice-swift.enum/front.md) — Specifies the camera on the front of the device.

### Initializers

- [init(rawValue:)](<cameradevice-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the camera to use

- [+ isCameraDeviceAvailable:](<iscameradeviceavailable(__).md>) — Queries whether the specified camera is available.
- [cameraDevice](cameradevice-swift.property.md) — The camera used by the image picker controller.
