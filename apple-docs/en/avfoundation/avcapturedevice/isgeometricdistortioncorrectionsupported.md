---
title: isGeometricDistortionCorrectionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionsupported.json'
content_hash: 'sha256:929372a11238f983'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isGeometricDistortionCorrectionSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether this device supports geometric distortion correction.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isGeometricDistortionCorrectionSupported: Bool { get }
```

## Discussion

Some devices benefit from geometric distortion correction (GDC), such as devices with a very wide field of view. GDC lessens the fisheye effect at the outer edge of the frame at the cost of losing a small amount of the horizontal field of view. When you enable GDC, the device upscales the corrected image to the original image size.

## See Also

### Enabling geometric distortion correction

- [geometricDistortionCorrectionEnabled](isgeometricdistortioncorrectionenabled.md) — A Boolean value that indicates whether geometric distortion correction is enabled for this device.
