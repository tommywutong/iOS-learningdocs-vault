---
title: cameraCalibrationData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avdepthdata/cameracalibrationdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avdepthdata/cameracalibrationdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdepthdata/cameracalibrationdata.json'
content_hash: 'sha256:2ca741efb1bd69b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDepthData](../avdepthdata.md)

# cameraCalibrationData

<sub>Instance Property</sub>

The imaging parameters with which this depth data was captured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var cameraCalibrationData: AVCameraCalibrationData? { get }
```

## Discussion

Using depth or disparity map data to render effects into a corresponding image or to perform computer vision tasks requires knowledge of the camera parameters that generated the depth data. Depth data captured by an [AVCaptureDevice](../avcapturedevice.md) object contains camera calibration data that includes such information.

> [!note] Note
> Depth data read from a file (see the [+ depthDataFromDictionaryRepresentation:error:](<init(fromdictionaryrepresentation_).md>) initializer) or transformed through arbitrary editing of its data map might not contain calibration data.
