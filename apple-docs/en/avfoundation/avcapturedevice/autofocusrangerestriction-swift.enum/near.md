---
title: AVCaptureDevice.AutoFocusRangeRestriction.near
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/near
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/near'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/autofocusrangerestriction-swift.enum/near.json'
content_hash: 'sha256:5aa902129588f445'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [AutoFocusRangeRestriction](../autofocusrangerestriction-swift.enum.md)

# AVCaptureDevice.AutoFocusRangeRestriction.near

<sub>Case</sub>

The device primarily attempts to focus on subjects near the camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
case near
```

## Discussion

You should use this value if your app uses [AVCaptureMetadataOutput](../../avcapturemetadataoutput.md) to recognize machine-readable codes.

## See Also

### Constants

- [AVCaptureAutoFocusRangeRestrictionNone](none.md) — The device attempts to focus on objects at any range.
- [AVCaptureAutoFocusRangeRestrictionFar](far.md) — The device primarily attempts to focus on subjects far away from the camera.
