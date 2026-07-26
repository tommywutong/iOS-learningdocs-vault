---
title: isGeometricDistortionCorrectionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isgeometricdistortioncorrectionenabled.json'
content_hash: 'sha256:61d263544163b762'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isGeometricDistortionCorrectionEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether geometric distortion correction is enabled for this device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isGeometricDistortionCorrectionEnabled: Bool { get set }
```

## Discussion

When the device supports geometric distortion correction (GDC), the default value is [true](../../swift/true.md).

## See Also

### Enabling geometric distortion correction

- [geometricDistortionCorrectionSupported](isgeometricdistortioncorrectionsupported.md) — A Boolean value that indicates whether this device supports geometric distortion correction.
