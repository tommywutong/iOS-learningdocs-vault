---
title: minAvailableVideoZoomFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minavailablevideozoomfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minavailablevideozoomfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minavailablevideozoomfactor.json'
content_hash: 'sha256:bd9cefb7862b05b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minAvailableVideoZoomFactor

<sub>Instance Property</sub>

The minimum zoom factor allowed in the current capture configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var minAvailableVideoZoomFactor: CGFloat { get }
```

## Discussion

On single-camera devices, this value is always `1.0`. On a dual-camera device, the allowed range of video zoom factors can change if the device is delivering depth data to one or more capture outputs.

Setting the [videoZoomFactor](videozoomfactor.md) property to (or calling the [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) method with) a value less than `1.0` always raises an exception. Setting the video zoom factor to a value between `1.0` and the minimum available zoom factor clamps the zoom setting to the minimum.

This property is key-value observable.

## See Also

### Inspecting zoom factors

- [maxAvailableVideoZoomFactor](maxavailablevideozoomfactor.md) — The maximum zoom factor allowed in the current capture configuration.
- [virtualDeviceSwitchOverVideoZoomFactors](virtualdeviceswitchovervideozoomfactors.md) — An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [dualCameraSwitchOverVideoZoomFactor](dualcameraswitchovervideozoomfactor.md) — The video zoom factor at which a dual camera device can automatically switch between cameras. _(deprecated)_
- [displayVideoZoomFactorMultiplier](displayvideozoomfactormultiplier.md) — A video zoom factor multiplier to use when displaying zoom information in a user interface.
