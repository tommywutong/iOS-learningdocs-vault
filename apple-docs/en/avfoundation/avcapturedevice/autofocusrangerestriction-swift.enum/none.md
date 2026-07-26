---
title: AVCaptureDevice.AutoFocusRangeRestriction.none
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/none
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/none'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/none.json'
content_hash: 'sha256:dc0e7afd1e9e8acc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [AutoFocusRangeRestriction](../autofocusrangerestriction-swift.enum.md)

# AVCaptureDevice.AutoFocusRangeRestriction.none

<sub>Case</sub>

The device attempts to focus on objects at any range.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case none
```

## Discussion

This value is the default, and the only value allowed on devices that do not support focus range restriction.

## See Also

### Constants

- [AVCaptureAutoFocusRangeRestrictionNear](near.md) — The device primarily attempts to focus on subjects near the camera.
- [AVCaptureAutoFocusRangeRestrictionFar](far.md) — The device primarily attempts to focus on subjects far away from the camera.
