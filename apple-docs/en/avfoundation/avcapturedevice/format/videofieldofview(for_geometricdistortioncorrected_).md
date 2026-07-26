---
title: 'videoFieldOfView(for:geometricDistortionCorrected:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/format/videofieldofview(for:geometricdistortioncorrected:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videofieldofview(for:geometricdistortioncorrected:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videofieldofview%28for%3Ageometricdistortioncorrected%3A%29.json'
content_hash: 'sha256:be315a470b9411c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFieldOfView(for:geometricDistortionCorrected:)

<sub>Instance Method</sub>

Indicates the horizontal field of view for an aspect ratio, either uncorrected or corrected for geometric distortion.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func videoFieldOfView(for aspectRatio: AVCaptureDevice.AspectRatio, geometricDistortionCorrected: Bool) -> Float
```

## Discussion

A float indicating the field of view for the corresponding [AspectRatio](../aspectratio.md). Set `AVCaptureDevice/geometricDistortionCorrected` to `true` to receive the field of view corrected for geometric distortion. If this device format does not support dynamic aspect ratio, this function returns `0`.

## See Also

### Determining dynamic aspect ratio support

- [supportedDynamicAspectRatios](supporteddynamicaspectratios.md) — Indicates the supported aspect ratios for the device format.
