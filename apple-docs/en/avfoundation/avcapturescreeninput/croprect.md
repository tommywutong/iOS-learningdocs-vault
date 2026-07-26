---
title: cropRect
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturescreeninput/croprect
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturescreeninput/croprect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturescreeninput/croprect.json'
content_hash: 'sha256:57bf25b9fb92dbed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureScreenInput](../avcapturescreeninput.md)

# cropRect

<sub>Instance Property</sub>

Indicates the bounding rectangle of the screen area to be captured, in pixels.

<sub>macOS</sub>

```swift
var cropRect: CGRect { get set }
```

## Discussion

By default, `AVCaptureScreenInput` captures the entire area of the displayID with which it is associated.

Set the value of this property to limit the capture rectangle to a subsection of the screen.

The rectangle should define a smaller section of the screen in the screen’s coordinate system. The origin (0,0) is the bottom-left corner of the screen.

## See Also

### Setting video capture options

- [minFrameDuration](minframeduration.md) — The screen input’s minimum frame duration.
- [scaleFactor](scalefactor.md) — Indicates the factor by which video buffers captured from the screen are to be scaled.
