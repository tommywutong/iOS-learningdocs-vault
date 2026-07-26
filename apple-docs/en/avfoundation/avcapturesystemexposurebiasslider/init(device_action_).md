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
doc_path: '/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:action:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:action:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesystemexposurebiasslider/init%28device%3Aaction%3A%29.json'
content_hash: 'sha256:64747305e1849f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSystemExposureBiasSlider](../avcapturesystemexposurebiasslider.md)

# init(device:action:)

<sub>Initializer</sub>

Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(device: AVCaptureDevice, action: @escaping @MainActor @Sendable (Float) -> Void)
```

## Parameters

- `device` — The capture device to control.

- `action` — An action the system calls on the main actor to handle changes to the device’s [exposureTargetBias](../avcapturedevice/exposuretargetbias.md) property.

## Discussion

The system only calls the specified action when the exposure bias slider changes the device’s [videoZoomFactor](../avcapturedevice/videozoomfactor.md) property value. If you need to react to other sources of changes to the exposure target bias, use key-value observation instead.

> [!important] Important
> Don’t change the capture device’s exposure target bias when the system calls the action.

## See Also

### Creating an exposure bias slider

- [- initWithDevice:](<init(device_).md>) — Creates a slider to control the exposure bias of the specified capture device.
