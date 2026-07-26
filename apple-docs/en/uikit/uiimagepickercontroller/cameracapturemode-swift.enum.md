---
title: UIImagePickerController.CameraCaptureMode
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiimagepickercontroller/cameracapturemode-swift.enum.json'
content_hash: 'sha256:bef7fd94c92f62e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIImagePickerController](../uiimagepickercontroller.md)

# UIImagePickerController.CameraCaptureMode

<sub>Enumeration</sub>

Constants that specify the category of media for the camera to capture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
enum CameraCaptureMode
```

## Overview

The constants in this enumeration are for use as values of the [cameraCaptureMode](cameracapturemode-swift.property.md) property.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIImagePickerControllerCameraCaptureModePhoto](cameracapturemode-swift.enum/photo.md) — Specifies that the camera captures still images.
- [UIImagePickerControllerCameraCaptureModeVideo](cameracapturemode-swift.enum/video.md) — Specifies that the camera captures movies.

### Initializers

- [init(rawValue:)](<cameracapturemode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring the camera capture mode

- [+ availableCaptureModesForCameraDevice:](<availablecapturemodes(for_).md>) — Retrieves the capture modes supported by the specified camera device.
- [cameraCaptureMode](cameracapturemode-swift.property.md) — The capture mode used by the camera.
