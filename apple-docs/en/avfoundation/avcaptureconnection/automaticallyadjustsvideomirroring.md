---
title: automaticallyAdjustsVideoMirroring
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/automaticallyadjustsvideomirroring.json'
content_hash: 'sha256:291bed08edbd1850'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# automaticallyAdjustsVideoMirroring

<sub>Instance Property</sub>

A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var automaticallyAdjustsVideoMirroring: Bool { get set }
```

## Discussion

For some session configurations, the connection mirrors the video data by default. When the value of this property is [true](../../swift/true.md), the value of [videoMirrored](isvideomirrored.md) may change, depending on the configuration of the session. For example, the value may change after switching to a different capture device input.

The default value is [true](../../swift/true.md).

## See Also

### Mirroring a video

- [supportsVideoMirroring](isvideomirroringsupported.md) — A Boolean value that indicates whether the connection supports video mirroring.
- [videoMirrored](isvideomirrored.md) — A Boolean value that indicates whether the connection horizontally flips the video flowing through it.
