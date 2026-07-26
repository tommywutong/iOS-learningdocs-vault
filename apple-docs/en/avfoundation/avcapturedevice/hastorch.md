---
title: hasTorch
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/hastorch
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/hastorch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/hastorch.json'
content_hash: 'sha256:d72b109f5d78cc59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# hasTorch

<sub>Instance Property</sub>

A Boolean value that specifies whether the capture device has a torch.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var hasTorch: Bool { get }
```

## Discussion

A torch is a light source, such as an LED flash, that’s available on the device and used for illuminating captured content or providing general illumination. This property reflects whether the current device has such illumination hardware built-in.

Even if the device has a torch, that torch might not be available for use, so check the value of the [torchAvailable](istorchavailable.md) property before using it.

This property is key-value observable.

## See Also

### Configuring torch settings

- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
