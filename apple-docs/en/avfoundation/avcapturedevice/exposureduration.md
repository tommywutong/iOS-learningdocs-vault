---
title: exposureDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposureduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposureduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposureduration.json'
content_hash: 'sha256:45e79ed6e684bf42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# exposureDuration

<sub>Instance Property</sub>

The length of time over which exposure takes place.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var exposureDuration: CMTime { get }
```

## Discussion

The exposure duration is between the active format’s [minExposureDuration](format/minexposureduration.md) and [maxExposureDuration](format/maxexposureduration.md).

To set the exposure duration, call the [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) method.

This property is key-value observable.

## See Also

### Configuring exposure manually

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) — Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [ISO](iso.md) — The current exposure ISO value.
- [lensAperture](lensaperture.md) — The size of the lens diaphragm.
- [activeMaxExposureDuration](activemaxexposureduration.md) — The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
