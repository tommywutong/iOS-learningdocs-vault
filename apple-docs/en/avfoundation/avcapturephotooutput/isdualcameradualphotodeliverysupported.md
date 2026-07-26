---
title: isDualCameraDualPhotoDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isdualcameradualphotodeliverysupported.json'
content_hash: 'sha256:0eb4fffa5472efb0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isDualCameraDualPhotoDeliverySupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output currently supports simultaneous photo capture with both cameras on a dual-camera device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDualCameraDualPhotoDeliverySupported: Bool { get }
```

## Discussion

Not all devices and capture formats support dual camera capture. This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes. If a camera or format change causes this property’s value to become [false](../../swift/false.md), the [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) property’s value also becomes [false](../../swift/false.md).

This property is key-value observable.

## See Also

### Configuring dual camera capture

- [dualCameraFusionSupported](isdualcamerafusionsupported.md) — A Boolean value indicating whether the capture output currently supports automatically combining image data on a dual camera device. _(deprecated)_
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for simultaneous photo capture with both cameras on a dual-camera device. _(deprecated)_
