---
title: metadata
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/metadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/metadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/metadata.json'
content_hash: 'sha256:0e2a83c96cf37003'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# metadata

<sub>Instance Property</sub>

A dictionary of metadata describing the captured image.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var metadata: [String : Any] { get }
```

## Discussion

See `CGImageProperties` for possible keys and values. Metadata captured with a photo may include image orientation, EXIF camera properties, and Live Photo metadata.

## See Also

### Accessing photo metadata

- [depthData](depthdata.md) — Depth or disparity map data captured with the photo.
- [cameraCalibrationData](cameracalibrationdata.md) — Calibration information for the camera device that captured the photo.
- [sourceDeviceType](sourcedevicetype.md) — The type of device that captured the photo.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte captured with the photo.
