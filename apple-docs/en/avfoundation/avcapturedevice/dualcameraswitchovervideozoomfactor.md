---
title: dualCameraSwitchOverVideoZoomFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/dualcameraswitchovervideozoomfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/dualcameraswitchovervideozoomfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/dualcameraswitchovervideozoomfactor.json'
content_hash: 'sha256:a2d5bf66d3ceb5a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# dualCameraSwitchOverVideoZoomFactor

<sub>Instance Property</sub>

The video zoom factor at which a dual camera device can automatically switch between cameras.

> [!warning] Deprecated
> Use [virtualDeviceSwitchOverVideoZoomFactors](virtualdeviceswitchovervideozoomfactors.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var dualCameraSwitchOverVideoZoomFactor: CGFloat { get }
```

## Discussion

A dual camera device (see [AVCaptureDeviceTypeBuiltInDualCamera](devicetype-swift.struct/builtindualcamera.md)) contains both wide-angle and telephoto cameras.

This property’s value is the zoom factor at which the zoomed field of view from the wide-angle camera matches the full field of view from the telephoto camera. When the [videoZoomFactor](videozoomfactor.md) setting meets or exceeds this value, the device can automatically chooses which camera provides output imagery (or automatically combine imagery from both to create final output) based on scene conditions. For zoom factors below this value, the device always uses imagery from the wide-angle camera.

On a single-camera device, this value is always `1.0`.

## See Also

### Inspecting zoom factors

- [minAvailableVideoZoomFactor](minavailablevideozoomfactor.md) — The minimum zoom factor allowed in the current capture configuration.
- [maxAvailableVideoZoomFactor](maxavailablevideozoomfactor.md) — The maximum zoom factor allowed in the current capture configuration.
- [virtualDeviceSwitchOverVideoZoomFactors](virtualdeviceswitchovervideozoomfactors.md) — An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [displayVideoZoomFactorMultiplier](displayvideozoomfactormultiplier.md) — A video zoom factor multiplier to use when displaying zoom information in a user interface.
