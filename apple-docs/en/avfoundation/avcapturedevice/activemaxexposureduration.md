---
title: activeMaxExposureDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activemaxexposureduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activemaxexposureduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activemaxexposureduration.json'
content_hash: 'sha256:ea23ab7d99ac9867'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeMaxExposureDuration

<sub>Instance Property</sub>

The maximum exposure duration, in seconds, defined in the autoexposure algorithm.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var activeMaxExposureDuration: CMTime { get set }
```

## Discussion

When you set the exposureMode to [AVCaptureExposureModeAutoExpose](exposuremode-swift.enum/autoexpose.md) or [AVCaptureExposureModeContinuousAutoExposure](exposuremode-swift.enum/continuousautoexposure.md), the autoexposure algorithm picks a default maximum exposure duration that’s tuned for the current configuration, balancing low light image quality with motion preservation. By querying or key-value observing this property, you can determine the current maximum exposure duration in use.

You may also override the default value by setting this property to a value between the format’s [minExposureDuration](format/minexposureduration.md) and [maxExposureDuration](format/maxexposureduration.md) values. The system throws an exception if you pass an out-of-bounds exposure value.

Setting the property to the special value of [invalid](../../coremedia/cmtime/invalid.md) resets the autoexposure maximum duration to the device’s default for your current configuration. When the device’s [activeFormat](activeformat.md) or the capture session’s [sessionPreset](../avcapturesession/sessionpreset.md) changes, this property resets to the default max exposure duration for the new format or session preset.

On some devices, the auto exposure algorithm picks a different maximum exposure duration for a given format depending on whether you used the [sessionPreset](../avcapturesession/sessionpreset.md) or [activeFormat](activeformat.md) APIs to set to set the format. To ensure uniform default handling of maximum exposure duration, set the value of a capture input’s [unifiedAutoExposureDefaultsEnabled](../avcapturedeviceinput/unifiedautoexposuredefaultsenabled.md) property to [true](../../swift/true.md).

## See Also

### Configuring exposure manually

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<setexposuremodecustom(duration_iso_completionhandler_).md>) — Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [exposureDuration](exposureduration.md) — The length of time over which exposure takes place.
- [ISO](iso.md) — The current exposure ISO value.
- [lensAperture](lensaperture.md) — The size of the lens diaphragm.
