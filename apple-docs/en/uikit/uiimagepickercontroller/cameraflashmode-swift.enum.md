---
title: UIImagePickerController.CameraFlashMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameraflashmode-swift.enum.json'
content_hash: 'sha256:d1ccf141c8b2ebc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.CameraFlashMode

<sub>Enumeration</sub>

Constants that specify the flash mode to use with the active camera.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum CameraFlashMode
```

## Overview

The constants in this enumeration are for use as values of the [cameraFlashMode](cameraflashmode-swift.property.md) property.

The behavior of the flash depends on the camera capture mode.

- For a [cameraCaptureMode](cameracapturemode-swift.property.md) value of [UIImagePickerControllerCameraCaptureModePhoto](cameracapturemode-swift.enum/photo.md), flash is used to transiently illuminate the subject during still image capture.
- For a [cameraCaptureMode](cameracapturemode-swift.property.md) value of [UIImagePickerControllerCameraCaptureModeVideo](cameracapturemode-swift.enum/video.md), flash is used to continuously illuminate the subject during movie capture.

For a given camera on a device, flash may or may not be available. You specify the active camera by way of the [cameraDevice](cameradevice-swift.property.md) property. You can determine if the active camera has flash available by calling the [+ isFlashAvailableForCameraDevice:](<isflashavailable(for_).md>) class method.

You can manipulate the flash directly to provide effects such as a strobe light. Present a picker interface set to use video capture mode. Then, turn the flash LED on or off by setting the [cameraFlashMode](cameraflashmode-swift.property.md) property to [UIImagePickerControllerCameraFlashModeOn](cameraflashmode-swift.enum/on.md) or [UIImagePickerControllerCameraFlashModeOff](cameraflashmode-swift.enum/off.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerCameraFlashModeOff](cameraflashmode-swift.enum/off.md) — Specifies that flash illumination is always off, no matter what the ambient light conditions are.
- [UIImagePickerControllerCameraFlashModeAuto](cameraflashmode-swift.enum/auto.md) — Specifies that the device should consider ambient light conditions to automatically determine whether or not to use flash illumination.
- [UIImagePickerControllerCameraFlashModeOn](cameraflashmode-swift.enum/on.md) — Specifies that flash illumination is always on, no matter what the ambient light conditions are.

### Initializers

- [init(rawValue:)](<cameraflashmode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the flash behavior

- [+ isFlashAvailableForCameraDevice:](<isflashavailable(for_).md>) — Queries whether the specified camera has flash illumination capability.
- [cameraFlashMode](cameraflashmode-swift.property.md) — The flash mode used by the active camera.
