---
title: AVCaptureControl
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturecontrol
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturecontrol'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturecontrol.json'
content_hash: 'sha256:93362f917bdcd575'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureControl

<sub>Class</sub>

An abstract base class for controls that interact with the camera system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureControl
```

## Overview

Capture controls provide the interface for interacting with the camera system from the Camera Control button on iPhone 16 devices. The framework provides several concrete subclasses of this class that allow apps to access built-in functionality and define custom controls.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVCaptureIndexPicker](avcaptureindexpicker.md), [AVCaptureSlider](avcaptureslider.md), [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md), [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Setting the enabled state

- [enabled](avcapturecontrol/isenabled.md) — A Boolean value that indicates whether this control supports user interaction.

## See Also

### Capture controls

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md) — Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md) — A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md) — A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [AVCaptureSlider](avcaptureslider.md) — A slider control that selects a value from a bounded range.
- [AVCaptureIndexPicker](avcaptureindexpicker.md) — A control for selecting from a set of mutually exclusive values by index.
