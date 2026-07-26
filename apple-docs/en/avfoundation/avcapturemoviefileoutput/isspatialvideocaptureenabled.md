---
title: isSpatialVideoCaptureEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturemoviefileoutput/isspatialvideocaptureenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturemoviefileoutput/isspatialvideocaptureenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturemoviefileoutput/isspatialvideocaptureenabled.json'
content_hash: 'sha256:f0c446c79f0ec648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md)

# isSpatialVideoCaptureEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether a movie file output captures spatial videos.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isSpatialVideoCaptureEnabled: Bool { get set }
```

## Discussion

Spatial capture lets you record your favorite moments in 3D for playback on Apple Vision Pro. This feature isn’t supported on all devices, so you can only enable this property when [spatialVideoCaptureSupported](isspatialvideocapturesupported.md) is [true](../../swift/true.md).

The default value is [false](../../swift/false.md).

## See Also

### Enabling spatial capture

- [spatialVideoCaptureSupported](isspatialvideocapturesupported.md) — A Boolean value that indicates whether a movie file output supports capturing spatial videos.
