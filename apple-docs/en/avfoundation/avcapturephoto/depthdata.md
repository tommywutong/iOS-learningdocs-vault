---
title: depthData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/depthdata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/depthdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/depthdata.json'
content_hash: 'sha256:a9c6e965ab23e0ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# depthData

<sub>Instance Property</sub>

Depth or disparity map data captured with the photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var depthData: AVDepthData? { get }
```

## Discussion

To request capture of depth data alongside a photo (on supported devices), set the [depthDataDeliveryEnabled](../avcapturephotosettings/isdepthdatadeliveryenabled.md) property of your photo settings object to [true](../../swift/true.md) when requesting photo capture. If you did not request depth data delivery, this property’s value is `nil`.

> [!note] Note
> If you set the [embedsDepthDataInPhoto](../avcapturephotosettings/embedsdepthdatainphoto.md) property of your photo object to [false](../../swift/false.md) when requesting photo capture, this property still provides depth data, but that data is not included when generating photo file data for output.

## See Also

### Accessing photo metadata

- [cameraCalibrationData](cameracalibrationdata.md) — Calibration information for the camera device that captured the photo.
- [sourceDeviceType](sourcedevicetype.md) — The type of device that captured the photo.
- [metadata](metadata.md) — A dictionary of metadata describing the captured image.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte captured with the photo.
