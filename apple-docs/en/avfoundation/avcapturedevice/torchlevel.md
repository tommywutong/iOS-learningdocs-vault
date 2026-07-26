---
title: torchLevel
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/torchlevel
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchlevel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/torchlevel.json'
content_hash: 'sha256:34c5eb04ac1e0edf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# torchLevel

<sub>Instance Property</sub>

The current torch brightness level.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var torchLevel: Float { get }
```

## Discussion

The value of this property is a floating-point number whose value is in the range 0.0 to 1.0. A torch level of 0.0 indicates that the torch is off. A torch level of 1.0 represents the theoretical maximum value, although the actual maximum value may be lower if the device is currently overheated.

This property is key-value observable.

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
