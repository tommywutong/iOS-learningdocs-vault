---
title: modelID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/modelid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/modelid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/modelid.json'
content_hash: 'sha256:9da48c6146b971df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# modelID

<sub>Instance Property</sub>

A model identifier for the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var modelID: String { get }
```

## Discussion

The value of this property is an identifier unique to all devices of the same model. The value is persistent across device connections and disconnections, and across different systems. For example, the model identifier of a built-in camera on two identical iPhone models is the same even though they’re different physical devices.

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
