---
title: isCameraSensorOrientationCompensationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/iscamerasensororientationcompensationenabled.json'
content_hash: 'sha256:23350e03fbf18a91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isCameraSensorOrientationCompensationEnabled

<sub>Instance Property</sub>

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isCameraSensorOrientationCompensationEnabled: Bool { get set }
```

## Discussion

A BOOL value indicating that still image buffers will be rotated to match the sensor orientation of earlier generation hardware.

Default is YES when cameraSensorOrientationCompensationSupported is YES. Set to NO if your app does not require sensor orientation compensation.

## See Also

### Configuring orientation compensation

- [cameraSensorOrientationCompensationSupported](iscamerasensororientationcompensationsupported.md)
