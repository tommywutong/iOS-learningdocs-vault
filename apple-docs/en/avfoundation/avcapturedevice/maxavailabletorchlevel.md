---
title: maxAvailableTorchLevel
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/maxavailabletorchlevel
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxavailabletorchlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/maxavailabletorchlevel.json'
content_hash: 'sha256:b77b1df8987f05a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# maxAvailableTorchLevel

<sub>Type Property</sub>

A constant that indicates to set the torch to its maximum level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class let maxAvailableTorchLevel: Float
```

## Discussion

Pass this value to the [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) method to set the torch to the maximum level currently available. Under thermal duress, the maximum available torch level may be less than 1.0.

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
