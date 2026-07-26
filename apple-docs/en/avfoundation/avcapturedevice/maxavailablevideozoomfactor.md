---
title: maxAvailableVideoZoomFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/maxavailablevideozoomfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/maxavailablevideozoomfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/maxavailablevideozoomfactor.json'
content_hash: 'sha256:e0e42515e493f2f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# maxAvailableVideoZoomFactor

<sub>Instance Property</sub>

The maximum zoom factor allowed in the current capture configuration.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var maxAvailableVideoZoomFactor: CGFloat { get }
```

## Discussion

On single-camera devices, this value is always equal to the device format’s [videoMaxZoomFactor](format/videomaxzoomfactor.md) value. On a dual-camera device, the allowed range of video zoom factors can change if the device is delivering depth data to one or more capture outputs.

Setting the [videoZoomFactor](videozoomfactor.md) property to (or calling the [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) method with) a value greater than the device format’s [videoMaxZoomFactor](format/videomaxzoomfactor.md) value always raises an exception. Setting the video zoom factor to a value between the maximum available zoom factor and the device format’s maximum clamps the zoom setting to the maximum available value.

This property is key-value observable.

## See Also

### Inspecting zoom factors

- [minAvailableVideoZoomFactor](minavailablevideozoomfactor.md) — The minimum zoom factor allowed in the current capture configuration.
- [virtualDeviceSwitchOverVideoZoomFactors](virtualdeviceswitchovervideozoomfactors.md) — An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [dualCameraSwitchOverVideoZoomFactor](dualcameraswitchovervideozoomfactor.md) — The video zoom factor at which a dual camera device can automatically switch between cameras. _(deprecated)_
- [displayVideoZoomFactorMultiplier](displayvideozoomfactormultiplier.md) — A video zoom factor multiplier to use when displaying zoom information in a user interface.
