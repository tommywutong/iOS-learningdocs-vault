---
title: isCameraSensorOrientationCompensationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+（10.0 起废弃）, iPadOS 26.0+（10.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/iscamerasensororientationcompensationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscamerasensororientationcompensationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/iscamerasensororientationcompensationsupported.json'
content_hash: 'sha256:fae637d7389939e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isCameraSensorOrientationCompensationSupported

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isCameraSensorOrientationCompensationSupported: Bool { get }
```

## Discussion

A read-only BOOL value indicating whether still image buffers may be rotated to match the sensor orientation of earlier generation hardware.

Value is YES for camera configurations which support compensation for the sensor orientation, which is applied to HEIC, JPEG, and uncompressed processed photos only; compensation is never applied to Bayer RAW or Apple ProRaw captures.

## See Also

### Configuring orientation compensation

- [cameraSensorOrientationCompensationEnabled](iscamerasensororientationcompensationenabled.md) _(deprecated)_
