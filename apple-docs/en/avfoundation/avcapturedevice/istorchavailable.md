---
title: isTorchAvailable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/istorchavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/istorchavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/istorchavailable.json'
content_hash: 'sha256:4587e5f88fd8d4c2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isTorchAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether the torch is currently available for use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isTorchAvailable: Bool { get }
```

## Discussion

The torch may become unavailable if, for example, the device overheats and needs to cool off.

This property is key-value observable.

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
