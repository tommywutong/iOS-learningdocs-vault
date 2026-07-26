---
title: currentISO
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/currentiso
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentiso'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/currentiso.json'
content_hash: 'sha256:d5dfa10a8973047a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# currentISO

<sub>Type Property</sub>

A constant to indicate not to specify a new ISO value, and instead set it to its current value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let currentISO: Float
```

## Discussion

A special value that you may pass as the ISO parameter of the [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) method to indicate that the caller doesn’t specify a value for the ISO property, and to instead set to its current value.

> [!note] Note
> A device may be adjusting ISO at the time of the call, in which case the value set may differ from the value of thee [ISO](iso.md) property.

## See Also

### Exposure constants

- [AVCaptureExposureDurationCurrent](currentexposureduration.md) — A special constant representing the current exposure duration setting.
