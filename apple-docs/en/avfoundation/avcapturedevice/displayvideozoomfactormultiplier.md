---
title: displayVideoZoomFactorMultiplier
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 14.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/displayvideozoomfactormultiplier
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/displayvideozoomfactormultiplier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/displayvideozoomfactormultiplier.json'
content_hash: 'sha256:60b7ac978d7a7d03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# displayVideoZoomFactorMultiplier

<sub>Instance Property</sub>

A video zoom factor multiplier to use when displaying zoom information in a user interface.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var displayVideoZoomFactorMultiplier: CGFloat { get }
```

## Discussion

Some system user interfaces, like the macOS Video Effects Menu, display a video zoom factor value in a way most appropriate for visual presentation, which might differ from the [videoZoomFactor](videozoomfactor.md) property value.

Your app can key-value observe this property to update the display video zoom factor values in its user interface to stay consistent with Apple’s system UIs.

## See Also

### Inspecting zoom factors

- [minAvailableVideoZoomFactor](minavailablevideozoomfactor.md) — The minimum zoom factor allowed in the current capture configuration.
- [maxAvailableVideoZoomFactor](maxavailablevideozoomfactor.md) — The maximum zoom factor allowed in the current capture configuration.
- [virtualDeviceSwitchOverVideoZoomFactors](virtualdeviceswitchovervideozoomfactors.md) — An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [dualCameraSwitchOverVideoZoomFactor](dualcameraswitchovervideozoomfactor.md) — The video zoom factor at which a dual camera device can automatically switch between cameras. _(deprecated)_
