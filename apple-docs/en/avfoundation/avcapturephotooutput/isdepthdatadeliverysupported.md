---
title: isDepthDataDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isdepthdatadeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isdepthdatadeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isdepthdatadeliverysupported.json'
content_hash: 'sha256:c7015f2a3bde2847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isDepthDataDeliverySupported

<sub>Instance Property</sub>

A Boolean value indicating whether the capture output currently supports depth data capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isDepthDataDeliverySupported: Bool { get }
```

## Discussion

Depth data captures a per-pixel map of scene depth information delivered alongside the photo image and optionally embedded in image file output. Depth data can be used for purposes such as applying depth-sensitive photo filter effects (like that seen in the iOS Camera app’s Portrait mode) and performing computer vision tasks.

Not all devices and capture formats support depth capture. This property’s value can change if the [sessionPreset](../avcapturesession/sessionpreset.md) property of the current capture session or the [activeFormat](../avcapturedevice/activeformat.md) property of the underlying capture device changes. If a camera or format change causes this property’s value to become [false](../../swift/false.md), the [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) property’s value also becomes [false](../../swift/false.md).

This property is key-value observable.

## See Also

### Configuring depth data capture

- [depthDataDeliveryEnabled](isdepthdatadeliveryenabled.md) — A Boolean value that specifies whether to configure the capture pipeline for depth data capture.
