---
title: AVCaptureVideoOrientation
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+（17.0 起废弃）, macOS 10.7+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturevideoorientation
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturevideoorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturevideoorientation.json'
content_hash: 'sha256:a969b58839e2c77e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureVideoOrientation

<sub>Enumeration</sub>

Constants indicating video orientation.

> [!warning] Deprecated
> See [videoRotationAngle](avcaptureconnection/videorotationangle.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
enum AVCaptureVideoOrientation
```

## Overview

You can set these constants to [videoOrientation](avcaptureconnection/videoorientation.md) for a connection that has an [AVCaptureVideoPreviewLayer](avcapturevideopreviewlayer.md) output.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [AVCaptureVideoOrientationPortrait](avcapturevideoorientation/portrait.md) — Indicates that video should be oriented vertically, top at the top.
- [AVCaptureVideoOrientationPortraitUpsideDown](avcapturevideoorientation/portraitupsidedown.md) — Indicates that video should be oriented vertically, top at the bottom.
- [AVCaptureVideoOrientationLandscapeRight](avcapturevideoorientation/landscaperight.md) — Indicates that video should be oriented horizontally, top on the left.
- [AVCaptureVideoOrientationLandscapeLeft](avcapturevideoorientation/landscapeleft.md) — Indicates that video should be oriented horizontally, top on the right.

### Initializers

- [init(rawValue:)](<avcapturevideoorientation/init(rawvalue_).md>)

## See Also

### Deprecated

- [videoStabilizationEnabled](avcaptureconnection/isvideostabilizationenabled.md) — A Boolean value that indicates whether video stabilization is active for the connection. _(deprecated)_
- [enablesVideoStabilizationWhenAvailable](avcaptureconnection/enablesvideostabilizationwhenavailable.md) — A Boolean value that indicates whether the system enables video stabilization when it’s available. _(deprecated)_
- [supportsVideoOrientation](avcaptureconnection/isvideoorientationsupported.md) — A Boolean value that indicates whether the connection supports changing the orientation of the video. _(deprecated)_
- [videoOrientation](avcaptureconnection/videoorientation.md) — An orientation that tells the connection how to rotate a video flowing through it. _(deprecated)_
