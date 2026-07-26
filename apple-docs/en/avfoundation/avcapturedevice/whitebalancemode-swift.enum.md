---
title: AVCaptureDevice.WhiteBalanceMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.enum.json'
content_hash: 'sha256:ec0997e4888613e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.WhiteBalanceMode

<sub>Enumeration</sub>

Constants to specify the white balance mode of a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum WhiteBalanceMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### White balance modes

- [AVCaptureWhiteBalanceModeLocked](whitebalancemode-swift.enum/locked.md) — A mode that locks the white balance state.
- [AVCaptureWhiteBalanceModeAutoWhiteBalance](whitebalancemode-swift.enum/autowhitebalance.md) — A mode that automatically manages white balance.
- [AVCaptureWhiteBalanceModeContinuousAutoWhiteBalance](whitebalancemode-swift.enum/continuousautowhitebalance.md) — A mode that continuously monitors white balance and adjusts when necessary.

### Initializers

- [init(rawValue:)](<whitebalancemode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring automatic white balance

- [- isWhiteBalanceModeSupported:](<iswhitebalancemodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [whiteBalanceMode](whitebalancemode-swift.property.md) — The current white balance mode.
