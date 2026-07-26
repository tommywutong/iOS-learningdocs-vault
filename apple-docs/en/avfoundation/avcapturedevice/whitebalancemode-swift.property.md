---
title: whiteBalanceMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/whitebalancemode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/whitebalancemode-swift.property.json'
content_hash: 'sha256:627df5fa3b70022a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# whiteBalanceMode

<sub>Instance Property</sub>

The current white balance mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var whiteBalanceMode: AVCaptureDevice.WhiteBalanceMode { get set }
```

## Discussion

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you’re done configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring automatic white balance

- [- isWhiteBalanceModeSupported:](<iswhitebalancemodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified white balance mode.
- [WhiteBalanceMode](whitebalancemode-swift.enum.md) — Constants to specify the white balance mode of a capture device.
