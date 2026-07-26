---
title: AVCaptureSystemExposureBiasSlider
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesystemexposurebiasslider
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesystemexposurebiasslider.json'
content_hash: 'sha256:f74e194aca48948a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSystemExposureBiasSlider

<sub>Class</sub>

A control that adjusts the exposure bias of a capture device within the system-recommended range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureSystemExposureBiasSlider
```

## Overview

This control defines its range by querying the [systemRecommendedExposureBiasRange](avcapturedevice/format/systemrecommendedexposurebiasrange.md) property of the device’s active format. If a device’s [activeFormat](avcapturedevice/activeformat.md) value changes, the slider updates its range with the new format’s system-recommended value.

To use this control, add it to the capture session by calling the session’s [- addControl:](<avcapturesession/addcontrol(__).md>) method.

## Relationships

- **Inherits From**: [AVCaptureControl](avcapturecontrol.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating an exposure bias slider

- [- initWithDevice:](<avcapturesystemexposurebiasslider/init(device_).md>) — Creates a slider to control the exposure bias of the specified capture device.
- [- initWithDevice:action:](<avcapturesystemexposurebiasslider/init(device_action_).md>) — Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.

## See Also

### Capture controls

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md) — Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [AVCaptureControl](avcapturecontrol.md) — An abstract base class for controls that interact with the camera system.
- [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md) — A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [AVCaptureSlider](avcaptureslider.md) — A slider control that selects a value from a bounded range.
- [AVCaptureIndexPicker](avcaptureindexpicker.md) — A control for selecting from a set of mutually exclusive values by index.
