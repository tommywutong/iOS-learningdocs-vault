---
title: focusMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/focusmode-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/focusmode-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/focusmode-swift.property.json'
content_hash: 'sha256:74a15e09106d14fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# focusMode

<sub>Instance Property</sub>

The capture device’s focus mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var focusMode: AVCaptureDevice.FocusMode { get set }
```

## Discussion

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

This property is key-value observable.

## See Also

### Configuring automatic focus

- [- isFocusModeSupported:](<isfocusmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusSupported](issmoothautofocussupported.md) — A Boolean value that indicates whether the device supports smooth autofocus.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
