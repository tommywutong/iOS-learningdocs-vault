---
title: currentExposureTargetBias
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/currentexposuretargetbias
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/currentexposuretargetbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/currentexposuretargetbias.json'
content_hash: 'sha256:5a3d43f99bba0cc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# currentExposureTargetBias

<sub>Type Property</sub>

A special constant that represents the current exposure bias value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let currentExposureTargetBias: Float
```

## Discussion

Pass this value to the [- setExposureTargetBias:completionHandler:](<setexposuretargetbias(__completionhandler_).md>) method to lock exposure bias to its current value, which disables autoexposure.

## See Also

### Adjusting exposure compensation

- [exposureTargetOffset](exposuretargetoffset.md) — The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [exposureTargetBias](exposuretargetbias.md) — The bias to apply to the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [maxExposureTargetBias](maxexposuretargetbias.md) — The maximum supported exposure bias, in exposure value (EV) units.
- [- setExposureTargetBias:completionHandler:](<setexposuretargetbias(__completionhandler_).md>) — Sets the bias to apply to the target exposure value.
