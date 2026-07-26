---
title: dynamicAspectRatio
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/dynamicaspectratio
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicaspectratio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/dynamicaspectratio.json'
content_hash: 'sha256:8ef2191043ffd577'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# dynamicAspectRatio

<sub>Instance Property</sub>

A key-value observable property indicating the current aspect ratio for a device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var dynamicAspectRatio: AVCaptureDevice.AspectRatio? { get }
```

## Discussion

This property is initialized to the first [AspectRatio](aspectratio.md) listed in the device’s activeFormat’s [supportedDynamicAspectRatios](format/supporteddynamicaspectratios.md) property. If the activeFormat’s [supportedDynamicAspectRatios](format/supporteddynamicaspectratios.md) is an empty array, this property returns nil.

## See Also

### Configuring dynamic aspect ratio

- [- setDynamicAspectRatio:completionHandler:](<setdynamicaspectratio(__completionhandler_).md>) — Updates the dynamic aspect ratio of the device.
- [AspectRatio](aspectratio.md) — String constants describing the different video aspect ratios you can configure for a particular device.
- [dynamicDimensions](dynamicdimensions.md) — A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.
