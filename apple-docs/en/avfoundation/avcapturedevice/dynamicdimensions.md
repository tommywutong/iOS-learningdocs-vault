---
title: dynamicDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/dynamicdimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/dynamicdimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/dynamicdimensions.json'
content_hash: 'sha256:8df7df0fadeb8ddf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# dynamicDimensions

<sub>Instance Property</sub>

A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var dynamicDimensions: CMVideoDimensions { get }
```

## Discussion

If the device’s activeFormat’s [supportedDynamicAspectRatios](format/supporteddynamicaspectratios.md) is an empty array, this property returns {0,0}.

## See Also

### Configuring dynamic aspect ratio

- [- setDynamicAspectRatio:completionHandler:](<setdynamicaspectratio(__completionhandler_).md>) — Updates the dynamic aspect ratio of the device.
- [AspectRatio](aspectratio.md) — String constants describing the different video aspect ratios you can configure for a particular device.
- [dynamicAspectRatio](dynamicaspectratio.md) — A key-value observable property indicating the current aspect ratio for a device.
