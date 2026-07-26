---
title: devices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/discoverysession/devices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/discoverysession/devices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/discoverysession/devices.json'
content_hash: 'sha256:13e099570fde7659'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DiscoverySession](../discoverysession.md)

# devices

<sub>Instance Property</sub>

A list of devices that match the search criteria of the discovery session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var devices: [AVCaptureDevice] { get }
```

## Discussion

Querying this property provides an array devices currently available on the system. The system sorts the device list according to the order you specified when you created the discovery session. If you created the session with a position of [AVCaptureDevicePositionUnspecified](../position-swift.enum/unspecified.md), the system further sorts them by position in the [Position](../position-swift.enum.md) enumeration.

Key-value observe this property to monitor changes to the device list.

## See Also

### Finding devices

- [supportedMultiCamDeviceSets](supportedmulticamdevicesets.md) — Sets of capture devices that you can use simultaneously in a multi-camera session.
