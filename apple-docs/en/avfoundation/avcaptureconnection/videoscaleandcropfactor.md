---
title: videoScaleAndCropFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/videoscaleandcropfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videoscaleandcropfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videoscaleandcropfactor.json'
content_hash: 'sha256:1fc71e49d0b20eaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoScaleAndCropFactor

<sub>Instance Property</sub>

The current scale and crop factor the video output uses.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoScaleAndCropFactor: CGFloat { get set }
```

## Discussion

The property only applies to a video connection. You can set this property to a value in the range `[1.0,` ``AVCaptureConnection/videoMaxScaleAndCropFactor```]`. A factor of `1.0` keeps the image at its original. Factors greater than `1.0` scale the image up and center-crop the image to its original dimensions.

## See Also

### Scaling a video

- [videoMaxScaleAndCropFactor](videomaxscaleandcropfactor.md) — The connection’s maximum video scale and crop factor.
