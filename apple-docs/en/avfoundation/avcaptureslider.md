---
title: AVCaptureSlider
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureslider
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureslider'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureslider.json'
content_hash: 'sha256:4f465df906d7e9c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureSlider

<sub>Class</sub>

A slider control that selects a value from a bounded range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureSlider
```

## Overview

Sliders are appropriate for controls that provide a single float value.

## Relationships

- **Inherits From**: [AVCaptureControl](avcapturecontrol.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a slider

- [init(_:symbolName:in:)](<avcaptureslider/init(__symbolname_in_).md>) — Creates a continuous slider control that selects a value from a bounded range.
- [init(_:symbolName:in:step:)](<avcaptureslider/init(__symbolname_in_step_).md>) — Creates a discrete slider control that selects a stepped value from a bounded range.
- [init(_:symbolName:values:)](<avcaptureslider/init(__symbolname_values_).md>) — Creates a discrete slider control that selects a value from a list.

### Handling interaction

- [setActionQueue(_:action:)](<avcaptureslider/setactionqueue(__action_).md>) — Sets the action to perform on the specified dispatch queue when the control’s value changes.

### Accessing the control value

- [value](avcaptureslider/value.md) — The current value of the slider.
- [prominentValues](avcaptureslider/prominentvalues-199dz.md) — Values in this array may receive unique visual representations or behaviors.
- [localizedValueFormat](avcaptureslider/localizedvalueformat.md) — A localized string that defines the presentation of the slider’s value.

### Setting an accessibility identifier

- [accessibilityIdentifier](avcaptureslider/accessibilityidentifier.md) — A string identifier for the slider.

### Inspecting presentation attributes

- [symbolName](avcaptureslider/symbolname.md) — The name of the SF Symbol that represents this control.
- [localizedTitle](avcaptureslider/localizedtitle.md) — A localized title that describes the control’s action.

## See Also

### Capture controls

- [Enhancing your app experience with the Camera Control](enhancing-your-app-experience-with-the-camera-control.md) — Provide direct access to your camera app’s features to help people quickly capture the perfect shot.
- [AVCaptureControl](avcapturecontrol.md) — An abstract base class for controls that interact with the camera system.
- [AVCaptureSystemZoomSlider](avcapturesystemzoomslider.md) — A control that adjusts the video zoom factor of a capture device within the system-recommended range.
- [AVCaptureSystemExposureBiasSlider](avcapturesystemexposurebiasslider.md) — A control that adjusts the exposure bias of a capture device within the system-recommended range.
- [AVCaptureIndexPicker](avcaptureindexpicker.md) — A control for selecting from a set of mutually exclusive values by index.
