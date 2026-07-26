---
title: inverseLensDistortionLookupTable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcameracalibrationdata/inverselensdistortionlookuptable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/inverselensdistortionlookuptable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcameracalibrationdata/inverselensdistortionlookuptable.json'
content_hash: 'sha256:21fa0185b2b9e6d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCameraCalibrationData](../avcameracalibrationdata.md)

# inverseLensDistortionLookupTable

<sub>Instance Property</sub>

A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var inverseLensDistortionLookupTable: Data? { get }
```

## Discussion

If you’ve rectified an image by removing the distortions characterized by the [lensDistortionLookupTable](lensdistortionlookuptable.md) property, and now wish to go back to a geometrically distorted image (for example, to render visual effects into the camera image or perform computer vision tasks such as scene reconstruction), use this inverse lookup table.

## See Also

### Correcting for lens distortion

- [lensDistortionLookupTable](lensdistortionlookuptable.md) — A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.
- [lensDistortionCenter](lensdistortioncenter.md) — The offset of the distortion center of the camera lens from the top-left corner of the image.
