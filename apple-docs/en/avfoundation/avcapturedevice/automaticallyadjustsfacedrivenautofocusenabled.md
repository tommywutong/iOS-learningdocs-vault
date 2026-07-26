---
title: automaticallyAdjustsFaceDrivenAutoFocusEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/automaticallyadjustsfacedrivenautofocusenabled.json'
content_hash: 'sha256:1e37f14cccd378ea'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# automaticallyAdjustsFaceDrivenAutoFocusEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var automaticallyAdjustsFaceDrivenAutoFocusEnabled: Bool { get set }
```

## Discussion

The value of this property defaults to [true](../../swift/true.md) for devices that support auto focus. If your app requires explicitly setting the state of [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md), set this value to [false](../../swift/false.md).

To set this property value, you must call the device’s [- lockForConfiguration:](<lockforconfiguration().md>) method to obtain exclusive access to configure it. Otherwise, attempting to set a value raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock.

## See Also

### Configuring automatic focus

- [- isFocusModeSupported:](<isfocusmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [focusMode](focusmode-swift.property.md) — The capture device’s focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusSupported](issmoothautofocussupported.md) — A Boolean value that indicates whether the device supports smooth autofocus.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
