---
title: isCameraSensorOrientationCompensationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationsupported.json'
content_hash: 'sha256:bc898249479f0410'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

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

- [cameraSensorOrientationCompensationEnabled](iscamerasensororientationcompensationenabled.md)
