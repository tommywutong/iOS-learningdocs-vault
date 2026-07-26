---
title: AVCameraCalibrationData
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcameracalibrationdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcameracalibrationdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcameracalibrationdata.json'
content_hash: 'sha256:14dda6485a15c0b8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCameraCalibrationData

<sub>Class</sub>

Information about the camera characteristics used to capture images and depth data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVCameraCalibrationData
```

## Overview

Information about the calibration of a camera—such as its pixel focal length, principal point, and lens distortion characteristics—helps to determine the geometric relationships between the camera device and the images it captures. You can use this information to accurately render visual effects into images produced by a camera or perform computer vision tasks such as correcting images for geometric distortions.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Mapping pixels to scene geometry

- [intrinsicMatrix](avcameracalibrationdata/intrinsicmatrix.md) — A matrix that relates a camera’s internal properties to an ideal pinhole-camera model.
- [intrinsicMatrixReferenceDimensions](avcameracalibrationdata/intrinsicmatrixreferencedimensions.md) — The image dimensions to which the camera’s intrinsic matrix values are relative.
- [extrinsicMatrix](avcameracalibrationdata/extrinsicmatrix.md) — A matrix relating a camera’s position and orientation to a world or scene coordinate system.
- [pixelSize](avcameracalibrationdata/pixelsize.md) — The size, in millimeters, of one image pixel.

### Correcting for lens distortion

- [lensDistortionLookupTable](avcameracalibrationdata/lensdistortionlookuptable.md) — A map of floating-point values describing radial distortions imparted by the camera lens, for use in rectifying camera images.
- [inverseLensDistortionLookupTable](avcameracalibrationdata/inverselensdistortionlookuptable.md) — A map of floating-point values describing radial distortions for use in reapplying camera geometry to a rectified image.
- [lensDistortionCenter](avcameracalibrationdata/lensdistortioncenter.md) — The offset of the distortion center of the camera lens from the top-left corner of the image.

## See Also

### Depth data capture

- [Capturing photos with depth](capturing-photos-with-depth.md) — Get a depth map with a photo to create effects like the system camera’s Portrait mode (on compatible devices).
- [Creating auxiliary depth data manually](creating-auxiliary-depth-data-manually.md) — Generate a depth image and attach it to your own image.
- [Capturing depth using the LiDAR camera](capturing-depth-using-the-lidar-camera.md) — Access the LiDAR camera on supporting devices to capture precise depth data.
- [AVCamFilter: Applying filters to a capture stream](avcamfilter-applying-filters-to-a-capture-stream.md) — Render a capture stream with rose-colored filtering and depth effects.
- [Streaming depth data from the TrueDepth camera](streaming-depth-data-from-the-truedepth-camera.md) — Visualize depth data in 2D and 3D from the TrueDepth camera.
- [Enhancing live video by leveraging TrueDepth camera data](enhancing-live-video-by-leveraging-truedepth-camera-data.md) — Apply your own background to a live capture feed streamed from the front-facing TrueDepth camera.
- [AVCaptureDepthDataOutput](avcapturedepthdataoutput.md) — A capture output that records scene depth information on compatible camera devices.
- [AVDepthData](avdepthdata.md) — A container for per-pixel distance or disparity information captured by compatible camera devices.
