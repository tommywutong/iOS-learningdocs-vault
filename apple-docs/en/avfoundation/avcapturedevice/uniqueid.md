---
title: uniqueID
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/uniqueid
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/uniqueid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/uniqueid.json'
content_hash: 'sha256:8046073e26892c7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# uniqueID

<sub>Instance Property</sub>

An identifier that uniquely identifies the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var uniqueID: String { get }
```

## Discussion

Capture devices have a unique identifier that persists on one system across device connections and disconnections, application restarts, and reboots of the system itself. You can store the value returned by this property to recall or track the status of a specific device in the future.

## See Also

### Identifying a device

- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
- [Position](position-swift.enum.md) — Constants that indicate the physical position of a capture device.
