---
title: isPortraitEffectSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/isportraiteffectsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/isportraiteffectsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/isportraiteffectsupported.json'
content_hash: 'sha256:b22ee29f22b1f098'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isPortraitEffectSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the format supports the Portrait Effect feature.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isPortraitEffectSupported: Bool { get }
```

## Discussion

Enabling a Portrait Effect applies a shallow depth-of-field effect to objects in the background. See the [portraitEffectEnabled](../isportraiteffectenabled.md) property of [AVCaptureDevice](../../avcapturedevice.md) for more information.

## See Also

### Determining Portrait Effects support

- [portraitEffectsMatteStillImageDeliverySupported](isportraiteffectsmattestillimagedeliverysupported.md) — A Boolean indicating whether the device supports portrait matte effects in still-image capture.
- [videoFrameRateRangeForPortraitEffect](videoframeraterangeforportraiteffect.md) — The range of frame rates available when Portrait Effect is active.
