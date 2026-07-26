---
title: lensAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/lensaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/lensaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/lensaperture.json'
content_hash: 'sha256:4f332c4918bef200'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# lensAperture

<sub>Instance Property</sub>

The size of the lens diaphragm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var lensAperture: Float { get }
```

## Discussion

The value of this property is a float indicating the size (the `f` number) of the lens diaphragm.

This value doesn’t change.

## See Also

### Configuring exposure manually

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) — Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [exposureDuration](exposureduration.md) — The length of time over which exposure takes place.
- [ISO](iso.md) — The current exposure ISO value.
- [activeMaxExposureDuration](activemaxexposureduration.md) — The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
