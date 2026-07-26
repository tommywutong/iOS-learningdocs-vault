---
title: cameraCalibrationData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/cameracalibrationdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/cameracalibrationdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/cameracalibrationdata.json'
content_hash: 'sha256:997acdb1b07604e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# cameraCalibrationData

<sub>Instance Property</sub>

Calibration information for the camera device that captured the photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var cameraCalibrationData: AVCameraCalibrationData? { get }
```

## Discussion

Camera calibration data is present only if you specified the [cameraCalibrationDataDeliveryEnabled](../avcapturephotosettings/iscameracalibrationdatadeliveryenabled.md) and [dualCameraDualPhotoDeliveryEnabled](../avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) settings when requesting capture. For camera calibration data in a capture that includes depth data, see the [AVDepthData](../avdepthdata.md) [cameraCalibrationData](../avdepthdata/cameracalibrationdata.md) property.

## See Also

### Accessing photo metadata

- [depthData](depthdata.md) — Depth or disparity map data captured with the photo.
- [sourceDeviceType](sourcedevicetype.md) — The type of device that captured the photo.
- [metadata](metadata.md) — A dictionary of metadata describing the captured image.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte captured with the photo.
