---
title: AVCaptureDevice.TorchMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/torchmode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/torchmode-swift.enum.json'
content_hash: 'sha256:cb980fe5c5d71e20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.TorchMode

<sub>Enumeration</sub>

Constants to specify the capture device’s torch mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum TorchMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Torch modes

- [AVCaptureTorchModeOff](torchmode-swift.enum/off.md) — The capture device torch is always off.
- [AVCaptureTorchModeOn](torchmode-swift.enum/on.md) — The capture device torch is always on.
- [AVCaptureTorchModeAuto](torchmode-swift.enum/auto.md) — The capture device continuously monitors light levels and uses the torch when necessary.

### Initializers

- [init(rawValue:)](<torchmode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
