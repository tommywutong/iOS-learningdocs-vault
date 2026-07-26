---
title: geometricDistortionCorrectedVideoFieldOfView
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/geometricdistortioncorrectedvideofieldofview
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/geometricdistortioncorrectedvideofieldofview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/geometricdistortioncorrectedvideofieldofview.json'
content_hash: 'sha256:9ac69f7cee846411'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# geometricDistortionCorrectedVideoFieldOfView

<sub>Instance Property</sub>

A horizontal field of view for the format after correction for geometric distortion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var geometricDistortionCorrectedVideoFieldOfView: Float { get }
```

## Discussion

If the capture device doesn’t support geometric distortion correction (GDC), the value of this property is equal to the value of [videoFieldOfView](videofieldofview.md).

## See Also

### Determining field of view

- [videoFieldOfView](videofieldofview.md) — Indicates the format’s horizontal field of view in degrees.
