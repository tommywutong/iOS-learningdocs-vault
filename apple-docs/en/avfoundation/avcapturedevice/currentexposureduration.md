---
title: currentExposureDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/currentexposureduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentexposureduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/currentexposureduration.json'
content_hash: 'sha256:600e951e586371f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# currentExposureDuration

<sub>Type Property</sub>

A special constant representing the current exposure duration setting.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let currentExposureDuration: CMTime
```

## Discussion

Pass this value to [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) to lock exposure duration to its current value (that’s, to disable autoexposure).

## See Also

### Exposure constants

- [AVCaptureISOCurrent](currentiso.md) — A constant to indicate not to specify a new ISO value, and instead set it to its current value.
