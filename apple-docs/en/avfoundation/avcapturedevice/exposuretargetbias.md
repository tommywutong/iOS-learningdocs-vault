---
title: exposureTargetBias
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposuretargetbias
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuretargetbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposuretargetbias.json'
content_hash: 'sha256:5146f25ccfe7081b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# exposureTargetBias

<sub>Instance Property</sub>

The bias to apply to the target exposure value, in exposure value (EV) units.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var exposureTargetBias: Float { get }
```

## Discussion

When the device exposure mode is [AVCaptureExposureModeContinuousAutoExposure](exposuremode-swift.enum/continuousautoexposure.md) or [AVCaptureExposureModeLocked](exposuremode-swift.enum/locked.md), the bias affects both metering ([exposureTargetOffset](exposuretargetoffset.md)), and the actual exposure level ([exposureDuration](exposureduration.md) and [ISO](iso.md)).  When the exposure mode is [AVCaptureExposureModeCustom](exposuremode-swift.enum/custom.md), it only affects metering.

This property is key-value observable.

## See Also

### Adjusting exposure compensation

- [exposureTargetOffset](exposuretargetoffset.md) — The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [maxExposureTargetBias](maxexposuretargetbias.md) — The maximum supported exposure bias, in exposure value (EV) units.
- [AVCaptureExposureTargetBiasCurrent](currentexposuretargetbias.md) — A special constant that represents the current exposure bias value.
- [- setExposureTargetBias:completionHandler:](<setexposuretargetbias(__completionhandler_).md>) — Sets the bias to apply to the target exposure value.
