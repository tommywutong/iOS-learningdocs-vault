---
title: isPortraitEffectActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isportraiteffectactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isportraiteffectactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isportraiteffectactive.json'
content_hash: 'sha256:4cb62b8b0fe88a43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isPortraitEffectActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the Portrait video effect is active on a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isPortraitEffectActive: Bool { get }
```

## Discussion

When active, the device blurs the background, simulating a shallow depth of field effect. The device also limits the values of its [activeVideoMinFrameDuration](activevideominframeduration.md) and [activeVideoMaxFrameDuration](activevideomaxframeduration.md) to the value that the device format’s [videoFrameRateRangeForPortraitEffect](format/videoframeraterangeforportraiteffect.md) specifies.

When a capture device’s [portraitEffectEnabled](isportraiteffectenabled.md) property value is [true](../../swift/true.md), it may also return [true](../../swift/true.md) for this property, depending on whether it supports the feature in its current configuration.

This property is key-value observable.

## See Also

### Inspecting the Portrait Effect settings

- [portraitEffectEnabled](isportraiteffectenabled.md) — A Boolean value that indicates whether the user enabled the Portrait video effect in Control Center.
