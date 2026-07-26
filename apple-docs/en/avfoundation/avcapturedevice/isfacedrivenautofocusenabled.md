---
title: isFaceDrivenAutoFocusEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isfacedrivenautofocusenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfacedrivenautofocusenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isfacedrivenautofocusenabled.json'
content_hash: 'sha256:42003e513a2751b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFaceDrivenAutoFocusEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the device has face-driven autofocus enabled.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isFaceDrivenAutoFocusEnabled: Bool { get set }
```

## Discussion

Face-driven auto focus takes a subject’s face into account when adjusting auto focus. For apps that link against iOS 15.4 or later, the value of this property defaults to [true](../../swift/true.md) for devices that support auto focus.

Before setting a value for this property, perform the following:

- Obtain exclusive access to the device by calling its [- lockForConfiguration:](<lockforconfiguration().md>) method.
- Set the value of the device’s [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) property to [false](../../swift/false.md).

Attempting to set a value before performing these steps results in an exception.

When you finish configuring the device, unlock it by calling its [- unlockForConfiguration](<unlockforconfiguration().md>) method.

> [!important] Important
> Updating the state of this property doesn’t initiate a focus change. After setting a new value, set an appropriate [focusMode](focusmode-swift.property.md) to apply the change.

## See Also

### Configuring automatic focus

- [- isFocusModeSupported:](<isfocusmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [focusMode](focusmode-swift.property.md) — The capture device’s focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusSupported](issmoothautofocussupported.md) — A Boolean value that indicates whether the device supports smooth autofocus.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
