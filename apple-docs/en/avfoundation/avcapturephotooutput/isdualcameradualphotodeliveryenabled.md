---
title: isDualCameraDualPhotoDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliveryenabled.json'
content_hash: 'sha256:25e43c6d166b8c85'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isDualCameraDualPhotoDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDualCameraDualPhotoDeliveryEnabled: Bool { get set }
```

## Discussion

Enabling this property (on a supported device) allows the capture output to deliver separate images from both the wide-angle and telephoto cameras in a single capture.

Dual photo delivery requires that a capture session set up its internal rendering pipeline differently. If you intend to capture with dual photo delivery at all, set this property to [true](../../swift/true.md) before calling the [AVCaptureSession](../avcapturesession.md) [- startRunning](<../avcapturesession/startrunning().md>) method. Changing this property while the session is running requires a lengthy reconfiguration of the capture render pipeline: Live Photo captures in progress will end immediately, unfulfilled photo requests will abort, and video preview will temporarily freeze.

You must enable this option before initiating a photo capture with the [dualCameraDualPhotoDeliveryEnabled](../avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) property of your photo settings object set to [true](../../swift/true.md). However, after you’ve enabled this option, you are free to issue photo capture requests both with and without dual photo delivery.

## See Also

### Configuring dual camera capture

- [dualCameraFusionSupported](isdualcamerafusionsupported.md) — A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device. _(deprecated)_
- [dualCameraDualPhotoDeliverySupported](isdualcameradualphotodeliverysupported.md) — A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_
