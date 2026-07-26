---
title: 'videoRotationAngleRelative(toDeviceOrientation:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationanglerelative(todeviceorientation:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationanglerelative(todeviceorientation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationanglerelative%28todeviceorientation%3A%29.json'
content_hash: 'sha256:de407ad0be1bac60'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# videoRotationAngleRelative(toDeviceOrientation:)

<sub>Instance Method</sub>

Returns a video rotation angle in degrees from this camera relative to the provided orientation.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func videoRotationAngleRelative(toDeviceOrientation deviceOrientation: AVCaptureVideoOrientation) -> CGFloat
```

## Discussion

The returned video rotation angle represents the amount by which photos or movies captured from the camera should be rotated to be upright relative to the provided orientation. A returned video rotation angle of 0 degrees means that the output will be in the camera’s unrotated, native sensor orientation. The returned video rotation angle for an orientation may differ between cameras. For example, some cameras are upright when the device is held with the port on the bottom, while others are upright when holding the device with the port on the left or right. External cameras return 0 degrees for all given video orientations because the relationship between the device and the camera is unknown.

The angle returned from this property is distinct from the angles returned by -videoRotationAngleForHorizonLevelCapture and -videoRotationAngleForHorizonLevelPreview because those return angles relative to the horizon which change dynamically as the device is physically rotated, while this returns the static angle relative to the provided orientation regardless of how the device is physically oriented at the time this method is called.
