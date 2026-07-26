---
title: videoFieldMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/videofieldmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videofieldmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videofieldmode.json'
content_hash: 'sha256:9d6ef7904fd17fc0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoFieldMode

<sub>Instance Property</sub>

A setting that tells the connection how to interlace video flowing through it.

<sub>macOS</sub>

```swift
var videoFieldMode: AVVideoFieldMode { get set }
```

## Discussion

The property only applies to a video connection and when [supportsVideoFieldMode](isvideofieldmodesupported.md) is [true](../../swift/true.md).

## See Also

### Interlacing video

- [supportsVideoFieldMode](isvideofieldmodesupported.md) — A Boolean value that indicates whether the connection supports setting a video field mode.
- [AVVideoFieldMode](../avvideofieldmode.md) — Constants that indicate which interlacing modes the connection applies to video flowing through it.
