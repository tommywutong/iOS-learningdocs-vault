---
title: maxExposureTargetBias
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/maxexposuretargetbias
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxexposuretargetbias'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/maxexposuretargetbias.json'
content_hash: 'sha256:73c72f321d2cefa3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# maxExposureTargetBias

<sub>Instance Property</sub>

The maximum supported exposure bias, in exposure value (EV) units.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maxExposureTargetBias: Float { get }
```

## See Also

### Adjusting exposure compensation

- [exposureTargetOffset](exposuretargetoffset.md) — The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [exposureTargetBias](exposuretargetbias.md) — The bias to apply to the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [AVCaptureExposureTargetBiasCurrent](currentexposuretargetbias.md) — A special constant that represents the current exposure bias value.
- [- setExposureTargetBias:completionHandler:](<setexposuretargetbias(__completionhandler_).md>) — Sets the bias to apply to the target exposure value.
