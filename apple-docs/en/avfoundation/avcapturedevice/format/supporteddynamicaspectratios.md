---
title: supportedDynamicAspectRatios
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/supporteddynamicaspectratios
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supporteddynamicaspectratios'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/supporteddynamicaspectratios.json'
content_hash: 'sha256:a153b8d14466bee1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# supportedDynamicAspectRatios

<sub>Instance Property</sub>

Indicates the supported aspect ratios for the device format.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var supportedDynamicAspectRatios: [AVCaptureDevice.AspectRatio] { get }
```

## Discussion

An array that describes the aspect ratios that are supported for this format. If this device format does not support dynamic aspect ratio, this property returns an empty array.

## See Also

### Determining dynamic aspect ratio support

- [- videoFieldOfViewForAspectRatio:geometricDistortionCorrected:](<videofieldofview(for_geometricdistortioncorrected_).md>) — Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.
