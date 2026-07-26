---
title: device
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/rotationcoordinator/device
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/device'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/device.json'
content_hash: 'sha256:eeadcb37a206729a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# device

<sub>Instance Property</sub>

The capture device the coordinator monitors to track its physical rotation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
weak var device: AVCaptureDevice? { get }
```

## Discussion

The coordinator updates its [videoRotationAngleForHorizonLevelCapture](videorotationangleforhorizonlevelcapture.md) property by monitoring the device’s physical rotation.

## See Also

### Inspecting a coordinator’s configuration

- [previewLayer](previewlayer.md) — The layer that displays a camera preview the coordinator calculates a video rotation angle for.
