---
title: position
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/position-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/position-swift.property.json'
content_hash: 'sha256:c3ce30ce7afb310b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# position

<sub>Instance Property</sub>

The physical position of the capture device hardware.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var position: AVCaptureDevice.Position { get }
```

## Discussion

This property value is key-value observable.

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
