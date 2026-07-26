---
title: 'isTorchModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/istorchmodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/istorchmodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/istorchmodesupported%28_%3A%29.json'
content_hash: 'sha256:4ed1363818fd9d0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isTorchModeSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the device supports the specified torch mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isTorchModeSupported(_ torchMode: AVCaptureDevice.TorchMode) -> Bool
```

## Parameters

- `torchMode` — The desired torch mode.

## Return Value

[true](../../swift/true.md) if the device supports the torch mode; otherwise, [false](../../swift/false.md).

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
