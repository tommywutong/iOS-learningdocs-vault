---
title: lensStabilizationStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/lensstabilizationstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/lensstabilizationstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/lensstabilizationstatus.json'
content_hash: 'sha256:a5e1a38d443ea28c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# lensStabilizationStatus

<sub>Instance Property</sub>

Information about the use of lens stabilization during bracketed photo capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var lensStabilizationStatus: AVCaptureDevice.LensStabilizationStatus { get }
```

## Discussion

This property applies only to capture results for which you requested optical image stabilization (OIS) across all frames of a bracketed photo capture (using the [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md) [lensStabilizationEnabled](../avcapturephotobracketsettings/islensstabilizationenabled.md) property).

If the device configuration does not support OIS, this property’s value is [AVCaptureLensStabilizationStatusUnsupported](../avcapturedevice/lensstabilizationstatus/unsupported.md). If OIS is supported, but this captured photo is not from a bracketed capture where OIS was requested, this property’s value is [AVCaptureLensStabilizationStatusOff](../avcapturedevice/lensstabilizationstatus/off.md). Otherwise, this property indicates how the device applied OIS across the duration of the bracketed capture.

## See Also

### Examining bracketed capture information

- [bracketSettings](bracketsettings.md) — The variations available for bracketed capture settings for this photo.
- [sequenceCount](sequencecount.md) — The 1-based index of this photo in a bracketed capture sequence.
- [LensStabilizationStatus](../avcapturedevice/lensstabilizationstatus.md) — Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.
