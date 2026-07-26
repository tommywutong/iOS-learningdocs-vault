---
title: autoFocusRangeRestriction
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.property.json'
content_hash: 'sha256:b2fb53e0810ca199'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# autoFocusRangeRestriction

<sub>Instance Property</sub>

A value that controls the allowable range for automatic focusing.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var autoFocusRangeRestriction: AVCaptureDevice.AutoFocusRangeRestriction { get set }
```

## Discussion

By default, a device capable of hardware focusing attempts to focus on objects at any distance. If you expect to focus primarily on near or far objects, set a range restriction to increase the speed and reduce the power consumption of automatic focusing, and to reduce the chance of focusing ambiguities.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Configuring automatic focus

- [- isFocusModeSupported:](<isfocusmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [focusMode](focusmode-swift.property.md) — The capture device’s focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusSupported](issmoothautofocussupported.md) — A Boolean value that indicates whether the device supports smooth autofocus.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
