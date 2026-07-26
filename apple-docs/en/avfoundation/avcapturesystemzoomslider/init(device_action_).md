---
title: 'init(device:action:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesystemzoomslider/init(device:action:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesystemzoomslider/init(device:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesystemzoomslider/init%28device%3Aaction%3A%29.json'
content_hash: 'sha256:5e519ecf6c6ad1d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSystemZoomSlider](../avcapturesystemzoomslider.md)

# init(device:action:)

<sub>Initializer</sub>

Creates a slider to control the zoom level of the specified capture device with an action to respond to zoom changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(device: AVCaptureDevice, action: @escaping @MainActor @Sendable (CGFloat) -> Void)
```

## Parameters

- `device` — The capture device to control.

- `action` — An action the system calls on the main actor to respond to changes to the device’s [videoZoomFactor](../avcapturedevice/videozoomfactor.md) property.

## Discussion

The system calls the specified action only when the zoom slider changes the device’s [videoZoomFactor](../avcapturedevice/videozoomfactor.md) property value. If your app needs to react to other sources of video zoom factor changes like [- rampToVideoZoomFactor:withRate:](<../avcapturedevice/ramp(tovideozoomfactor_withrate_).md>), use key-value observation instead.

> [!important] Important
> Don’t change the capture device’s video zoom factor when the system calls the action.

## See Also

### Creating a zoom slider

- [- initWithDevice:](<init(device_).md>) — Creates a slider to control the video zoom factor of a capture device.
