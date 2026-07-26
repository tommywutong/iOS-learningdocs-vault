---
title: AVCaptureDevice.ExposureMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposuremode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposuremode-swift.enum.json'
content_hash: 'sha256:f27608520c39a14c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.ExposureMode

<sub>Enumeration</sub>

Constants that specify the exposure mode of a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum ExposureMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Exposure modes

- [AVCaptureExposureModeLocked](exposuremode-swift.enum/locked.md) — A mode that locks exposure for the device.
- [AVCaptureExposureModeAutoExpose](exposuremode-swift.enum/autoexpose.md) — A mode that automatically adjusts the exposure one time, and then locks exposure for the device.
- [AVCaptureExposureModeContinuousAutoExposure](exposuremode-swift.enum/continuousautoexposure.md) — A mode that continuously monitors exposure levels and automatically adjusts exposure when necessary.
- [AVCaptureExposureModeCustom](exposuremode-swift.enum/custom.md) — A mode where an app manually sets the exposure duration and ISO values.

### Initializers

- [init(rawValue:)](<exposuremode-swift.enum/init(rawvalue_).md>)

## See Also

### Managing the exposure mode

- [- isExposureModeSupported:](<isexposuremodesupported(__).md>) — Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [exposureMode](exposuremode-swift.property.md) — The exposure mode for the device.
