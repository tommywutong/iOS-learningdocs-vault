---
title: lensDistortionCenter
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcameracalibrationdata/lensdistortioncenter
source_url: 'https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/lensdistortioncenter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcameracalibrationdata/lensdistortioncenter.json'
content_hash: 'sha256:319a701c8d914989'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCameraCalibrationData](../avcameracalibrationdata.md)

# lensDistortionCenter

<sub>Instance Property</sub>

The offset of the distortion center of the camera lens from the top-left corner of the image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var lensDistortionCenter: CGPoint { get }
```

## Discussion

Due to geometric distortions in the image, the center of the distortion may not be equal to the optical center (principal point) of the lens. When making an image rectilinear, use the distortion center rather than the optical center of the image.

## See Also

### Correcting for lens distortion

- [lensDistortionLookupTable](lensdistortionlookuptable.md) — A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.
- [inverseLensDistortionLookupTable](inverselensdistortionlookuptable.md) — A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.
