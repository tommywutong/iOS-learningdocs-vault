---
title: isVideoOrientationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（17.0 起废弃）, iPadOS 4.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 10.7+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/isvideoorientationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideoorientationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideoorientationsupported.json'
content_hash: 'sha256:9df94995ff2d99a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoOrientationSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection supports changing the orientation of the video.

> [!warning] Deprecated
> Use [- isVideoRotationAngleSupported:](<isvideorotationanglesupported(__).md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isVideoOrientationSupported: Bool { get }
```

## See Also

### Deprecated

- [videoStabilizationEnabled](isvideostabilizationenabled.md) — A Boolean value that indicates whether video stabilization is active for the connection. _(deprecated)_
- [enablesVideoStabilizationWhenAvailable](enablesvideostabilizationwhenavailable.md) — A Boolean value that indicates whether the system enables video stabilization when it’s available. _(deprecated)_
- [videoOrientation](videoorientation.md) — An orientation that tells the connection how to rotate a video flowing through it. _(deprecated)_
- [AVCaptureVideoOrientation](../avcapturevideoorientation.md) — Constants indicating video orientation. _(deprecated)_
