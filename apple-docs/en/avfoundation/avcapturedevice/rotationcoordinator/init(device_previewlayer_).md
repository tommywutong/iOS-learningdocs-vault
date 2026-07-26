---
title: 'init(device:previewLayer:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/rotationcoordinator/init(device:previewlayer:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/init(device:previewlayer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/init%28device%3Apreviewlayer%3A%29.json'
content_hash: 'sha256:5c92ff99cb52765a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# init(device:previewLayer:)

<sub>Initializer</sub>

Creates a coordinator that provides separate compensation angles for content your app takes with a capture device, and for your app’s camera preview.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(device: AVCaptureDevice, previewLayer: CALayer?)
```

## Parameters

- `device` — A capture device the new coordinator monitors to track its physical rotation to calculate its [videoRotationAngleForHorizonLevelCapture](videorotationangleforhorizonlevelcapture.md) property.

- `previewLayer` — A layer that displays a camera preview the new coordinator monitors to calculate its [videoRotationAngleForHorizonLevelPreview](videorotationangleforhorizonlevelpreview.md) property.
