---
title: AVCaptureSystemZoomSlider
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturesystemzoomslider
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesystemzoomslider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesystemzoomslider.json'
content_hash: 'sha256:9bd91dcb5171d659'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSystemZoomSlider

<sub>Class</sub>

A control that adjusts the video zoom factor of a capture device within the system-recommended range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureSystemZoomSlider
```

## Overview

The system sets the slider’s range to the value of the [systemRecommendedVideoZoomRange](avcapturedevice/format/systemrecommendedvideozoomrange.md) property of the device’s active format. If a device’s [activeFormat](avcapturedevice/activeformat.md) value changes, the slider updates its range to the new format’s recommendation.

To use this control, add it to the capture session by calling the session’s [- addControl:](<avcapturesession/addcontrol(__).md>) method.

## Relationships

- **Inherits From**: [AVCaptureControl](avcapturecontrol.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a zoom slider

- [- initWithDevice:](<avcapturesystemzoomslider/init(device_).md>) — Creates a slider to control the video zoom factor of a capture device.
- [- initWithDevice:action:](<avcapturesystemzoomslider/init(device_action_).md>) — Creates a slider to control the zoom level of the specified capture device with an action to respond to zoom changes.

## See Also

### Capture controls

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md) — Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [AVCaptureControl](avcapturecontrol.md) — An abstract base class for controls that interact with the camera system.
- [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md) — A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [AVCaptureSlider](avcaptureslider.md) — A slider control that selects a value from a bounded range.
- [AVCaptureIndexPicker](avcaptureindexpicker.md) — A control for selecting from a set of mutually exclusive values by index.
