---
title: cameraCalibrationDataLensCollection
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avspatialvideoconfiguration-c.class/cameracalibrationdatalenscollection
source_url: 'https://developer.apple.com/documentation/avfoundation/avspatialvideoconfiguration-c.class/cameracalibrationdatalenscollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avspatialvideoconfiguration-c.class/cameracalibrationdatalenscollection.json'
content_hash: 'sha256:c93065c4a24f6dfa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSpatialVideoConfiguration](../avspatialvideoconfiguration-c.class.md)

# cameraCalibrationDataLensCollection

<sub>Instance Property</sub>

Specifies intrinsic and extrinsic parameters for single or multiple lenses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
@property (atomic, copy, nullable) NSArray<NSDictionary<NSString *,id> *> * cameraCalibrationDataLensCollection;
```

## Discussion

The property value is an array of dictionaries describing the camera calibration data for each lens. The camera calibration data includes intrinsics and extrinics with other parameters.  This property is only applicable when the projection kind is kCMTagProjectionTypeParametricImmersive.  Can be nil if the value is unknown.

## See Also

### Modifying the configuration

- [cameraSystemBaseline](camerasystembaseline.md) — Specifies the distance between centers of the lenses of the camera system that created the video.
- [disparityAdjustment](disparityadjustment.md) — Specifies a relative shift of the left and right images, which changes the zero parallax plane.
- [horizontalFieldOfView](horizontalfieldofview.md) — Specifies horizontal field of view in thousandths of a degree. Can be nil if the value is unknown.
