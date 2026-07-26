---
title: horizontalFieldOfView
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialvideoconfiguration-swift.struct/horizontalfieldofview
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/horizontalfieldofview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/horizontalfieldofview.json'
content_hash: 'sha256:f90945694a36aabf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)

# horizontalFieldOfView

<sub>Instance Property</sub>

Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var horizontalFieldOfView: UInt32?
```

## See Also

### Modifying the configuration

- [cameraCalibrationDataLensCollection](cameracalibrationdatalenscollection.md) — Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [cameraSystemBaseline](camerasystembaseline.md) — Specifies the distance between centers of the lenses of the camera system that created the video.
- [disparityAdjustment](disparityadjustment.md) — Specifies a relative shift of the left and right images, which changes the zero parallax plane.
