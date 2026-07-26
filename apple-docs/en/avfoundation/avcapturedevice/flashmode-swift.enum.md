---
title: AVCaptureDevice.FlashMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/flashmode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/flashmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/flashmode-swift.enum.json'
content_hash: 'sha256:5ab27eb21ffba618'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.FlashMode

<sub>Enumeration</sub>

Constants that specify the flash modes of a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum FlashMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Flash modes

- [AVCaptureFlashModeOff](flashmode-swift.enum/off.md) — A mode that indicates the flash is off.
- [AVCaptureFlashModeOn](flashmode-swift.enum/on.md) — A mode that indicates the flash is on.
- [AVCaptureFlashModeAuto](flashmode-swift.enum/auto.md) — A mode that indicates the device continuously monitors light levels and uses the flash when necessary.

### Initializers

- [init(rawValue:)](<flashmode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring flash settings

- [hasFlash](hasflash.md) — A Boolean value that indicates whether the capture device has a flash.
- [flashAvailable](isflashavailable.md) — A Boolean value that indicates whether the flash is currently available for use.
- [flashActive](isflashactive.md) — A Boolean value that indicates whether the flash is currently active. _(deprecated)_
- [flashMode](flashmode-swift.property.md) — The device’s current flash mode. _(deprecated)_
- [- isFlashModeSupported:](<isflashmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the given flash mode. _(deprecated)_
