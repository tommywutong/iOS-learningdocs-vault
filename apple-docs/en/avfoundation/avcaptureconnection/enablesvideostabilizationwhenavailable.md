---
title: enablesVideoStabilizationWhenAvailable
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（8.0 起废弃）, iPadOS 6.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/enablesvideostabilizationwhenavailable
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/enablesvideostabilizationwhenavailable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/enablesvideostabilizationwhenavailable.json'
content_hash: 'sha256:9330b17591c12a5c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# enablesVideoStabilizationWhenAvailable

<sub>Instance Property</sub>

A Boolean value that indicates whether the system enables video stabilization when it’s available.

> [!warning] Deprecated
> Use the [preferredVideoStabilizationMode](preferredvideostabilizationmode.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var enablesVideoStabilizationWhenAvailable: Bool { get set }
```

## See Also

### Deprecated

- [videoStabilizationEnabled](isvideostabilizationenabled.md) — A Boolean value that indicates whether video stabilization is active for the connection. _(deprecated)_
- [supportsVideoOrientation](isvideoorientationsupported.md) — A Boolean value that indicates whether the connection supports changing the orientation of the video. _(deprecated)_
- [videoOrientation](videoorientation.md) — An orientation that tells the connection how to rotate a video flowing through it. _(deprecated)_
- [AVCaptureVideoOrientation](../avcapturevideoorientation.md) — Constants indicating video orientation. _(deprecated)_
