---
title: AVCaptureDevice.RotationCoordinator
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/rotationcoordinator
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator.json'
content_hash: 'sha256:4304927bdf1dc4a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.RotationCoordinator

<sub>Class</sub>

A class that monitors the physical orientation of a capture device and provides adjustment angles to keep images level, relative to gravity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class RotationCoordinator
```

## Overview

Correctly rotate the photos and movies your app captures, and optionally, a live camera preview, by applying a coordinator’s [videoRotationAngleForHorizonLevelCapture](rotationcoordinator/videorotationangleforhorizonlevelcapture.md) and [videoRotationAngleForHorizonLevelPreview](rotationcoordinator/videorotationangleforhorizonlevelpreview.md) properties, respectively. Each rotation coordinator instance updates its properties so that your app can observe them and immediately apply them to the relevant components.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a rotation coordinator

- [- initWithDevice:previewLayer:](<rotationcoordinator/init(device_previewlayer_).md>) — Creates a coordinator that provides separate compensation angles for content your app takes with a capture device, and for your app’s camera preview.

### Compensating for a device’s rotation

- [videoRotationAngleForHorizonLevelCapture](rotationcoordinator/videorotationangleforhorizonlevelcapture.md) — An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.
- [videoRotationAngleForHorizonLevelPreview](rotationcoordinator/videorotationangleforhorizonlevelpreview.md) — An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.

### Inspecting a coordinator’s configuration

- [device](rotationcoordinator/device.md) — The capture device the coordinator monitors to track its physical rotation.
- [previewLayer](rotationcoordinator/previewlayer.md) — The layer that displays a camera preview the coordinator calculates a video rotation angle for.

### Instance Methods

- [- videoRotationAngleRelativeToDeviceOrientation:](<rotationcoordinator/videorotationanglerelative(todeviceorientation_).md>) — Returns a video rotation angle in degrees from this camera relative to the provided orientation. _(beta)_
