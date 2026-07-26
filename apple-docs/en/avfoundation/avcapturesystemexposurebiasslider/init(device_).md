---
title: 'init(device:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesystemexposurebiasslider/init(device:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesystemexposurebiasslider/init%28device%3A%29.json'
content_hash: 'sha256:d7f3cc3f276dd53e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSystemExposureBiasSlider](../avcapturesystemexposurebiasslider.md)

# init(device:)

<sub>Initializer</sub>

Creates a slider to control the exposure bias of the specified capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
init(device: AVCaptureDevice)
```

## Parameters

- `device` — The capture device to control.

## Discussion

You can only create an exposure bias slider with a device that support’s setting its [exposureTargetBias](../avcapturedevice/exposuretargetbias.md) property value.

## See Also

### Creating an exposure bias slider

- [- initWithDevice:action:](<init(device_action_).md>) — Creates a slider to control the exposure bias of the specified capture device with an action to respond to exposure bias changes.
