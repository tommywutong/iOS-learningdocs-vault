---
title: torchMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/torchmode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/torchmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/torchmode-swift.property.json'
content_hash: 'sha256:1cbc88f0a67aae3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# torchMode

<sub>Instance Property</sub>

The current torch mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var torchMode: AVCaptureDevice.TorchMode { get set }
```

## Discussion

Setting the value of this property also sets the torch level to its maximum current value.

Before setting the value of this property, call the [- isTorchModeSupported:](<istorchmodesupported(__).md>) method to make sure the device supports the desired mode. Setting the device to an unsupported torch mode results in the raising of an exception. For a list of possible values for this property, see [TorchMode](torchmode-swift.enum.md).

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring torch settings

- [hasTorch](hastorch.md) — A Boolean value that specifies whether the capture device has a torch.
- [torchAvailable](istorchavailable.md) — A Boolean value that indicates whether the torch is currently available for use.
- [torchActive](istorchactive.md) — A Boolean value that indicates whether the device’s torch is currently active.
- [torchLevel](torchlevel.md) — The current torch brightness level.
- [TorchMode](torchmode-swift.enum.md) — Constants to specify the capture device’s torch mode.
- [- isTorchModeSupported:](<istorchmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified torch mode.
- [- setTorchModeOnWithLevel:error:](<settorchmodeon(level_).md>) — Sets the illumination level when in torch mode.
- [AVCaptureMaxAvailableTorchLevel](maxavailabletorchlevel.md) — A constant that indicates to set the torch to its maximum level.
