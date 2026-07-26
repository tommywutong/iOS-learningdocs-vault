---
title: AVCaptureDevice.Position
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/position-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/position-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/position-swift.enum.json'
content_hash: 'sha256:49140bdbdd51d959'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.Position

<sub>Enumeration</sub>

Constants that indicate the physical position of a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Position
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Positions

- [AVCaptureDevicePositionFront](position-swift.enum/front.md) — A position on the user-facing side of an iOS device.
- [AVCaptureDevicePositionBack](position-swift.enum/back.md) — A position on the subject-facing side of an iOS device.
- [AVCaptureDevicePositionUnspecified](position-swift.enum/unspecified.md) — A position that’s unspecified.

### Initializers

- [init(rawValue:)](<position-swift.enum/init(rawvalue_).md>)

## See Also

### Identifying a device

- [uniqueID](uniqueid.md) — An identifier that uniquely identifies the device.
- [modelID](modelid.md) — A model identifier for the device.
- [localizedName](localizedname.md) — A localized device name for display in the user interface.
- [manufacturer](manufacturer.md) — A human-readable string for the manufacturer of the device.
- [deviceType](devicetype-swift.property.md) — The type of device, such as a built-in microphone or wide-angle camera.
- [DeviceType](devicetype-swift.struct.md) — A structure that defines the device types the framework supports.
- [position](position-swift.property.md) — The physical position of the capture device hardware.
