---
title: isVideoFieldModeSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/isvideofieldmodesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideofieldmodesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideofieldmodesupported.json'
content_hash: 'sha256:a0f4fc690844de03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoFieldModeSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection supports setting a video field mode.

<sub>macOS</sub>

```swift
var isVideoFieldModeSupported: Bool { get }
```

## Discussion

The property only applies to a video connection’s [videoFieldMode](videofieldmode.md) property.

## See Also

### Interlacing video

- [videoFieldMode](videofieldmode.md) — A setting that tells the connection how to interlace video flowing through it.
- [AVVideoFieldMode](../avvideofieldmode.md) — Constants that indicate which interlacing modes the connection applies to video flowing through it.
