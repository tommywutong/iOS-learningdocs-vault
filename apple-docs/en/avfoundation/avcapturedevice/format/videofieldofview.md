---
title: videoFieldOfView
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/videofieldofview
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/videofieldofview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/videofieldofview.json'
content_hash: 'sha256:d8abb8cc8bf596f8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# videoFieldOfView

<sub>Instance Property</sub>

Indicates the format’s horizontal field of view in degrees.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoFieldOfView: Float { get }
```

## Discussion

Returns zero if the format’s field of view is unknown.

## See Also

### Determining field of view

- [geometricDistortionCorrectedVideoFieldOfView](geometricdistortioncorrectedvideofieldofview.md) — A horizontal field of view for the format after correction for geometric distortion.
