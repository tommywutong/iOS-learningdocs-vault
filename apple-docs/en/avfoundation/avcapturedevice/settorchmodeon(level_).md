---
title: 'setTorchModeOn(level:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/settorchmodeon(level:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/settorchmodeon(level:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/settorchmodeon%28level%3A%29.json'
content_hash: 'sha256:3dd31c867c2585be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setTorchModeOn(level:)

<sub>Instance Method</sub>

Sets the illumination level when in torch mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setTorchModeOn(level torchLevel: Float) throws
```

## Parameters

- `torchLevel` — The new torch mode level. This value must be a floating-point number between `0.0` and `1.0`. To set the torch mode level to the currently available maximum, specify the constant [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) for this parameter.

## Discussion

This method sets the torch mode to [AVCaptureTorchModeOn](torchmode-swift.enum/on.md) and sets the level to the specified value. If the device doesn’t support this mode or if you specify a value for `torchLevel` that’s outside the accepted range, this method raises an exception. If the torch value is within the accepted range but greater than the currently supported maximum—perhaps because the device is overheating—this method returns [false](../../swift/false.md).

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, calling this method raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [torchMode](torchmode-swift.property.md) — The current torch mode.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
