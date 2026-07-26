---
title: intrinsicMatrixReferenceDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcameracalibrationdata/intrinsicmatrixreferencedimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/intrinsicmatrixreferencedimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcameracalibrationdata/intrinsicmatrixreferencedimensions.json'
content_hash: 'sha256:06abf67032babd9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCameraCalibrationData](../avcameracalibrationdata.md)

# intrinsicMatrixReferenceDimensions

<sub>Instance Property</sub>

The image dimensions to which the camera’s intrinsic matrix values are relative.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var intrinsicMatrixReferenceDimensions: CGSize { get }
```

## Discussion

The [intrinsicMatrix](intrinsicmatrix.md) property measures focal length and principal point offset in pixels, but those values are meaningful only in the context of an image of this size.

## See Also

### Mapping pixels to scene geometry

- [intrinsicMatrix](intrinsicmatrix.md) — A matrix that relates a camera’s internal properties to an ideal pinhole-camera model.
- [extrinsicMatrix](extrinsicmatrix.md) — A matrix relating a camera’s position and orientation to a world or scene coordinate system.
- [pixelSize](pixelsize.md) — The size, in millimeters, of one image pixel.
