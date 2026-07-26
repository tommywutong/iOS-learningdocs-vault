---
title: manufacturer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.9+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/manufacturer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/manufacturer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/manufacturer.json'
content_hash: 'sha256:4c01beea0c3600f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# manufacturer

<sub>Instance Property</sub>

A human-readable string for the manufacturer of the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var manufacturer: String { get }
```

## Discussion

You can use this property to identify capture devices by manufacturer. For all Apple devices, the value of this property is `Apple Inc.`

> [!tip] Tip
> Devices from third-party manufacturers may not provide identifying text, in which case the value of this property is an empty string.

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
