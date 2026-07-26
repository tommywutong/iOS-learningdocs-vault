---
title: videoMaxScaleAndCropFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/videomaxscaleandcropfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videomaxscaleandcropfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videomaxscaleandcropfactor.json'
content_hash: 'sha256:49c66da5a7f74bd6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoMaxScaleAndCropFactor

<sub>Instance Property</sub>

The connection’s maximum video scale and crop factor.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoMaxScaleAndCropFactor: CGFloat { get }
```

## Discussion

The value defines the largest value you can set the [videoScaleAndCropFactor](videoscaleandcropfactor.md) property to, which only applies to a video connection.

## See Also

### Scaling a video

- [videoScaleAndCropFactor](videoscaleandcropfactor.md) — The current scale and crop factor the video output uses.
