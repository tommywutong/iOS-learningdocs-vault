---
title: exposureTargetOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/exposuretargetoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/exposuretargetoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/exposuretargetoffset.json'
content_hash: 'sha256:16200960f86b4bf3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# exposureTargetOffset

<sub>Instance Property</sub>

The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var exposureTargetOffset: Float { get }
```

## Discussion

The value of property indicates the difference between the metered exposure level of the current scene and the target exposure value.

This property is key-value observable.

## See Also

### Adjusting exposure compensation

- [exposureTargetBias](exposuretargetbias.md) — The bias to apply to the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [maxExposureTargetBias](maxexposuretargetbias.md) — The maximum supported exposure bias, in exposure value (EV) units.
- [AVCaptureExposureTargetBiasCurrent](currentexposuretargetbias.md) — A special constant that represents the current exposure bias value.
- [- setExposureTargetBias:completionHandler:](<setexposuretargetbias(__completionhandler_).md>) — Sets the bias to apply to the target exposure value.
