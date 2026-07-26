---
title: previewLayer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/rotationcoordinator/previewlayer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/previewlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/previewlayer.json'
content_hash: 'sha256:67236afa53be22d1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# previewLayer

<sub>Instance Property</sub>

The layer that displays a camera preview the coordinator calculates a video rotation angle for.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
weak var previewLayer: CALayer? { get }
```

## Discussion

The coordinator updates its [videoRotationAngleForHorizonLevelPreview](videorotationangleforhorizonlevelpreview.md) property by monitoring the layer and the physical rotation of [device](device.md).

## See Also

### Inspecting a coordinator’s configuration

- [device](device.md) — The capture device the coordinator monitors to track its physical rotation.
