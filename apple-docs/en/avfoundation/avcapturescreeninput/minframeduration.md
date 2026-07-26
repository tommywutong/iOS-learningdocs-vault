---
title: minFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/minframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/minframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/minframeduration.json'
content_hash: 'sha256:84bf291f2b1375ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# minFrameDuration

<sub>Instance Property</sub>

The screen input’s minimum frame duration.

<sub>macOS</sub>

```swift
var minFrameDuration: CMTime { get set }
```

## Discussion

The `minFrameDuration` is the reciprocal of its maximum frame rate.

You use this property to request a maximum frame rate at which the input produces video frames. The requested rate may not be achievable due to overall bandwidth, so actual frame rates may be lower.

## See Also

### Setting video capture options

- [cropRect](croprect.md) — Indicates the bounding rectangle of the screen area to be captured, in pixels.
- [scaleFactor](scalefactor.md) — Indicates the factor by which video buffers captured from the screen are to be scaled.
