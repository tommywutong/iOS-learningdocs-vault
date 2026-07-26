---
title: iso
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/iso
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iso'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iso.json'
content_hash: 'sha256:490d4a2bfda38000'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# iso

<sub>Instance Property</sub>

The current exposure ISO value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var iso: Float { get }
```

## Discussion

This property controls the sensor’s sensitivity to light by applying a gain value to the signal. This value is between the active format’s [minISO](format/miniso.md) and [maxISO](format/maxiso.md) values. Higher values result in noisier images.

To set the ISO, call the [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) method.

This property is key-value observable.

## See Also

### Configuring exposure manually

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) — Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [exposureDuration](exposureduration.md) — The length of time over which exposure takes place.
- [lensAperture](lensaperture.md) — The size of the lens diaphragm.
- [activeMaxExposureDuration](activemaxexposureduration.md) — The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
