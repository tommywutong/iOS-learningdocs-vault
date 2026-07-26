---
title: isVideoStabilizationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+（8.0 起废弃）, iPadOS 6.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/isvideostabilizationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideostabilizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideostabilizationenabled.json'
content_hash: 'sha256:b0ff0fee12d2cb11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoStabilizationEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether video stabilization is active for the connection.

> [!warning] Deprecated
> Use the [activeVideoStabilizationMode](activevideostabilizationmode.md) property instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isVideoStabilizationEnabled: Bool { get }
```

## See Also

### Deprecated

- [enablesVideoStabilizationWhenAvailable](enablesvideostabilizationwhenavailable.md) — A Boolean value that indicates whether the system enables video stabilization when it’s available. _(deprecated)_
- [supportsVideoOrientation](isvideoorientationsupported.md) — A Boolean value that indicates whether the connection supports changing the orientation of the video. _(deprecated)_
- [videoOrientation](videoorientation.md) — An orientation that tells the connection how to rotate a video flowing through it. _(deprecated)_
- [AVCaptureVideoOrientation](../avcapturevideoorientation.md) — Constants indicating video orientation. _(deprecated)_
