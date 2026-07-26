---
title: exposureMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposuremode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuremode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposuremode-swift.property.json'
content_hash: 'sha256:16fc7153538c26fb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# exposureMode

<sub>Instance Property</sub>

The exposure mode for the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var exposureMode: AVCaptureDevice.ExposureMode { get set }
```

## Discussion

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Managing the exposure mode

- [- isExposureModeSupported:](<isexposuremodesupported(__).md>) — Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [ExposureMode](exposuremode-swift.enum.md) — Constants that specify the exposure mode of a capture device.
