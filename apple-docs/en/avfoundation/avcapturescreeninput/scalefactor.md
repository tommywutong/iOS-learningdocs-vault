---
title: scaleFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/scalefactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/scalefactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/scalefactor.json'
content_hash: 'sha256:d4c634365f8bbac4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# scaleFactor

<sub>Instance Property</sub>

Indicates the factor by which video buffers captured from the screen are to be scaled.

<sub>macOS</sub>

```swift
var scaleFactor: CGFloat { get set }
```

## Discussion

By default, `AVCaptureScreenInput` captures the video buffers from the display at a scale factor of 1.0 (no scaling). Set this property to scale the buffers by a given factor; for example a 320x240 capture area with a scaleFactor of `2.0` produces video buffers at 640x480.

## See Also

### Setting video capture options

- [minFrameDuration](minframeduration.md) — The screen input’s minimum frame duration.
- [cropRect](croprect.md) — Indicates the bounding rectangle of the screen area to be captured, in pixels.
