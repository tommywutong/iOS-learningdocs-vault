---
title: isStillImageStabilizationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isstillimagestabilizationsupported.json'
content_hash: 'sha256:7490c97f8d8fd48e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isStillImageStabilizationSupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output currently supports automatic stabilization for still image capture.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isStillImageStabilizationSupported: Bool { get }
```

## Discussion

To capture a photo with image stabilization, set the [autoStillImageStabilizationEnabled](../avcapturephotosettings/isautostillimagestabilizationenabled.md) property of your photo settings object. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device. If a device does not support still image stabilization, set the [autoStillImageStabilizationEnabled](../avcapturephotosettings/isautostillimagestabilizationenabled.md) property has no effect (that is, the resolved [stillImageStabilizationEnabled](../avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md) setting will always be [false](../../swift/false.md)).

> [!note] Note
> This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.
