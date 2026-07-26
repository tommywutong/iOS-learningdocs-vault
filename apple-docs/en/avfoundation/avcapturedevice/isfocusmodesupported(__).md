---
title: 'isFocusModeSupported(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/isfocusmodesupported(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfocusmodesupported(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isfocusmodesupported%28_%3A%29.json'
content_hash: 'sha256:738fbd52a3b0da64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFocusModeSupported(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the device supports the specified focus mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func isFocusModeSupported(_ focusMode: AVCaptureDevice.FocusMode) -> Bool
```

## Parameters

- `focusMode` — A focus mode to query.

## Return Value

[true](../../swift/true.md) if the device supports the focus mode; otherwise, [false](../../swift/false.md).

## See Also

### Configuring automatic focus

- [focusMode](focusmode-swift.property.md) — The capture device’s focus mode.
- [FocusMode](focusmode-swift.enum.md) — Constants to specify the focus mode of a capture device.
- [smoothAutoFocusSupported](issmoothautofocussupported.md) — A Boolean value that indicates whether the device supports smooth autofocus.
- [smoothAutoFocusEnabled](issmoothautofocusenabled.md) — A Boolean value that indicates whether smooth autofocus is in an enabled state on the device.
- [faceDrivenAutoFocusEnabled](isfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device has face-driven autofocus enabled.
- [automaticallyAdjustsFaceDrivenAutoFocusEnabled](automaticallyadjustsfacedrivenautofocusenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autofocus.
- [autoFocusRangeRestrictionSupported](isautofocusrangerestrictionsupported.md) — A Boolean value that indicates whether the device supports focus range restrictions.
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
- [AutoFocusRangeRestriction](autofocusrangerestriction-swift.enum.md) — Constants to specify the autofocus range of a capture device.
