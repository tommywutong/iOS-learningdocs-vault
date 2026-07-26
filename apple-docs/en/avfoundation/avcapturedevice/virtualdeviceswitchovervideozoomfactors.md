---
title: virtualDeviceSwitchOverVideoZoomFactors
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/virtualdeviceswitchovervideozoomfactors
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/virtualdeviceswitchovervideozoomfactors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/virtualdeviceswitchovervideozoomfactors.json'
content_hash: 'sha256:c021c1c519d50e68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# virtualDeviceSwitchOverVideoZoomFactors

<sub>Instance Property</sub>

An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var virtualDeviceSwitchOverVideoZoomFactors: [NSNumber] { get }
```

## Discussion

This property contains zoom factors at which the field of view of one constituent device matches the full field of view of the next constituent device. The number of switched-over video zoom factors is always one fewer than the count of the [constituentDevices](constituentdevices.md) property. These factors progress in the same order as the devices listed in that property.

The value of this property is an empty array for nonvirtual devices.

## See Also

### Inspecting zoom factors

- [minAvailableVideoZoomFactor](minavailablevideozoomfactor.md) — The minimum zoom factor allowed in the current capture configuration.
- [maxAvailableVideoZoomFactor](maxavailablevideozoomfactor.md) — The maximum zoom factor allowed in the current capture configuration.
- [dualCameraSwitchOverVideoZoomFactor](dualcameraswitchovervideozoomfactor.md) — The video zoom factor at which a dual camera device can automatically switch between cameras. _(deprecated)_
- [displayVideoZoomFactorMultiplier](displayvideozoomfactormultiplier.md) — A video zoom factor multiplier to use when displaying zoom information in a user interface.
