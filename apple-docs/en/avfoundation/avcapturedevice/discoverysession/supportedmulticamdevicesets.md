---
title: supportedMultiCamDeviceSets
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/discoverysession/supportedmulticamdevicesets
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/supportedmulticamdevicesets'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/discoverysession/supportedmulticamdevicesets.json'
content_hash: 'sha256:7afa164d69a62977'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DiscoverySession](../discoverysession.md)

# supportedMultiCamDeviceSets

<sub>Instance Property</sub>

Sets of capture devices that you can use simultaneously in a multi-camera session.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var supportedMultiCamDeviceSets: [Set<AVCaptureDevice>] { get }
```

## Discussion

You may use multiple cameras as device inputs to an [AVCaptureMultiCamSession](../../avcapturemulticamsession.md), as long as one of the supported multi-camera device sets includes the device.

## See Also

### Finding devices

- [devices](devices.md) — A list of devices that match the search criteria of the discovery session.
