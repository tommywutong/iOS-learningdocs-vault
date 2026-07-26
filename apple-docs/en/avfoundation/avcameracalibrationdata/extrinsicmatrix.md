---
title: extrinsicMatrix
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcameracalibrationdata/extrinsicmatrix
source_url: 'https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata/extrinsicmatrix'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcameracalibrationdata/extrinsicmatrix.json'
content_hash: 'sha256:5f382817a78dc6c3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCameraCalibrationData](../avcameracalibrationdata.md)

# extrinsicMatrix

<sub>Instance Property</sub>

A matrix relating a camera’s position and orientation to a world or scene coordinate system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var extrinsicMatrix: matrix_float4x3 { get }
```

## Discussion

The extrinsic matrix consists of a unitless 3 x 3 rotation matrix (`R`) on the left and a 3 x 1 column vector translation (`t`) on the right. The translation vector’s units are millimeters.

![](../../../../attachments/92babba2b0619b872714b9dcb8889260/media-2902624@2x.png)

The camera’s pose is expressed with respect to a reference camera (camera-to-world view). If the rotation matrix is an identity matrix, then this camera is the reference camera.

> [!note] Note
> A [matrix_float4x3](../../simd/matrix_float4x3.md) matrix is column major with 3 rows and 4 columns.

## See Also

### Mapping pixels to scene geometry

- [intrinsicMatrix](intrinsicmatrix.md) — A matrix that relates a camera’s internal properties to an ideal pinhole-camera model.
- [intrinsicMatrixReferenceDimensions](intrinsicmatrixreferencedimensions.md) — The image dimensions to which the camera’s intrinsic matrix values are relative.
- [pixelSize](pixelsize.md) — The size, in millimeters, of one image pixel.
