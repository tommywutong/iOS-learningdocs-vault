---
title: deviceType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.property.json'
content_hash: 'sha256:e0bb50886db723f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# deviceType

<sub>Instance Property</sub>

The type of device, such as a built-in microphone or wide-angle camera.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var deviceType: AVCaptureDevice.DeviceType { get }
```

## Discussion

Use the [+ defaultDeviceWithDeviceType:mediaType:position:](<default(__for_position_).md>) method or the [DiscoverySession](discoverysession.md) class to find capture devices by device type.

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
