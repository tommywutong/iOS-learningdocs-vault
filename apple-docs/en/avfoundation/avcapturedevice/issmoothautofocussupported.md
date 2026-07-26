---
title: isSmoothAutoFocusSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/issmoothautofocussupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/issmoothautofocussupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/issmoothautofocussupported.json'
content_hash: 'sha256:edc4cca4b880c845'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isSmoothAutoFocusSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports smooth autofocus.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isSmoothAutoFocusSupported: Bool { get }
```

## Discussion

The smooth focusing mode is available only on compatible devices. If this property’s value is [false](../../swift/false.md), setting the value of [smoothAutoFocusEnabled](issmoothautofocusenabled.md) to [true](../../swift/true.md) raises an exception.

## See Also

### Configuring automatic focus

- [- isFocusModeSupported:](<isfocusmodesupported(__).md>) — Returns a Boolean value that indicates whether the device supports the specified focus mode.
- [focusMode](focusmode-swift.property.md) — The capture device’s focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
