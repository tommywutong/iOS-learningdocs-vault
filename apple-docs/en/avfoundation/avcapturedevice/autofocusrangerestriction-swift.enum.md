---
title: AVCaptureDevice.AutoFocusRangeRestriction
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum.json'
content_hash: 'sha256:64f047b2269205b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.AutoFocusRangeRestriction

<sub>Enumeration</sub>

Constants to specify the autofocus range of a capture device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
enum AutoFocusRangeRestriction
```

## Overview

If you expect to focus primarily on near or far objects, you can use the [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) property to provide a hint to the focusing system. This approach makes autofocus faster, more power efficient, and less error prone. A restriction prioritizes focusing at distances in the specified range, but doesn’t prevent focusing elsewhere if the device finds no focus point within that range.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [AVCaptureAutoFocusRangeRestrictionNone](autofocusrangerestriction-swift.enum/none.md) — The device attempts to focus on objects at any range.
- [AVCaptureAutoFocusRangeRestrictionNear](autofocusrangerestriction-swift.enum/near.md) — The device primarily attempts to focus on subjects near the camera.
- [AVCaptureAutoFocusRangeRestrictionFar](autofocusrangerestriction-swift.enum/far.md) — The device primarily attempts to focus on subjects far away from the camera.

### Initializers

- [init(rawValue:)](<autofocusrangerestriction-swift.enum/init(rawvalue_).md>)

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
- [autoFocusRangeRestriction](autofocusrangerestriction-swift.property.md) — A value that controls the allowable range for automatic focusing.
