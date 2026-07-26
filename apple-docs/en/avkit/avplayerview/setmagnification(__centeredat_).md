---
title: 'setMagnification(_:centeredAt:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerview/setmagnification(_:centeredat:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/setmagnification(_:centeredat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/setmagnification%28_%3Acenteredat%3A%29.json'
content_hash: 'sha256:acacc07be4685ed0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# setMagnification(_:centeredAt:)

<sub>Instance Method</sub>

Scales the video’s view by a specified factor, and centers the result on a specified point.

<sub>macOS</sub>

```swift
func setMagnification(_ magnification: CGFloat, centeredAt point: CGPoint)
```

## Parameters

- `magnification` — A factor by which to scale the video’s view.

- `point` — A point in view space on which to center magnification.

## Discussion

The supported magnification range is `1.0` to `64.0`. The system zooms using nearest neighbor interpolation after it scales the content past a certain factor.

## See Also

### Magnifying video

- [allowsMagnification](allowsmagnification.md) — A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.
- [magnification](magnification.md) — The factor by which the video’s view is currently scaled.
