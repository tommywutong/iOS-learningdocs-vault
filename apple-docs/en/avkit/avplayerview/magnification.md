---
title: magnification
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/magnification
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/magnification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/magnification.json'
content_hash: 'sha256:a892c0b756f6ed8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# magnification

<sub>Instance Property</sub>

The factor by which the video’s view is currently scaled.

<sub>macOS</sub>

```swift
var magnification: CGFloat { get set }
```

## Discussion

The supported magnification range is `1.0` to `64.0`. The system zooms using nearest neighbor interpolation after it scales the content past a certain factor.

The default value is `1.0`.

## See Also

### Magnifying video

- [allowsMagnification](allowsmagnification.md) — A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.
- [- setMagnification:centeredAtPoint:](<setmagnification(__centeredat_).md>) — Scales the video’s view by a specified factor, and centers the result on a specified point.
