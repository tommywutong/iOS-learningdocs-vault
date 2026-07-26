---
title: cameraSystemBaseline
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialvideoconfiguration-swift.struct/camerasystembaseline
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/camerasystembaseline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-swift.struct/camerasystembaseline.json'
content_hash: 'sha256:414aee9094954ff7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-swift.struct.md)

# cameraSystemBaseline

<sub>Instance Property</sub>

Specifies the distance between centers of the lenses of the camera system that created the video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cameraSystemBaseline: UInt32?
```

## Discussion

The distance is in micrometers or thousandths of a millimeter. Can be nil if the value is unknown.

## See Also

### Modifying the configuration

- [cameraCalibrationDataLensCollection](cameracalibrationdatalenscollection.md) — Specifies intrinsic and extrinsic parameters for single or multiple lenses.
- [disparityAdjustment](disparityadjustment.md) — Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [horizontalFieldOfView](horizontalfieldofview.md) — Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.
