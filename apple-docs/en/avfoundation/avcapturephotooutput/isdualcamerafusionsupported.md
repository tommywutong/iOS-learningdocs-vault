---
title: isDualCameraFusionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+（13.0 起废弃）, iPadOS 10.2+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/isdualcamerafusionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcamerafusionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isdualcamerafusionsupported.json'
content_hash: 'sha256:f0676e6ecd0cb4d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isDualCameraFusionSupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDualCameraFusionSupported: Bool { get }
```

## Discussion

On devices equipped with a dual camera, image fusion combines samples from both cameras to produce a higher quality image.

To capture a photo with image fusion, set the [autoDualCameraFusionEnabled](../avcapturephotosettings/isautodualcamerafusionenabled.md) property of your photo settings object. If a device does not support image fusion, setting the [autoDualCameraFusionEnabled](../avcapturephotosettings/isautodualcamerafusionenabled.md) property has no effect (that is, the resolved [dualCameraFusionEnabled](../avcaptureresolvedphotosettings/isdualcamerafusionenabled.md) setting will always be false).

> [!note] Note
> This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes.

This property supports key-value observing.

## See Also

### Configuring dual camera capture

- [dualCameraDualPhotoDeliverySupported](isdualcameradualphotodeliverysupported.md) — A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_
