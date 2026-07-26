---
title: videoFrameRateRangeForPortraitEffect
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videoframeraterangeforportraiteffect
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforportraiteffect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videoframeraterangeforportraiteffect.json'
content_hash: 'sha256:9ece9060f1d9278d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFrameRateRangeForPortraitEffect

<sub>Instance Property</sub>

The range of frame rates available when Portrait Effect is active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoFrameRateRangeForPortraitEffect: AVFrameRateRange? { get }
```

## Discussion

Devices may support a limited range of frame rates when Portrait Effect is active. If a device format doesn’t support Portrait Effect, the value of this property is `nil`.

## See Also

### Determining Portrait Effects support

- [portraitEffectSupported](isportraiteffectsupported.md) — A Boolean value that indicates whether the format supports the Portrait Effect feature.
- [portraitEffectsMatteStillImageDeliverySupported](isportraiteffectsmattestillimagedeliverysupported.md) — A Boolean indicating whether the device supports portrait matte effects in still-image capture.
