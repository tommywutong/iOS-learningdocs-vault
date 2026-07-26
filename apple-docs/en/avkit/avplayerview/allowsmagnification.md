---
title: allowsMagnification
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/allowsmagnification
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/allowsmagnification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/allowsmagnification.json'
content_hash: 'sha256:c0c63ef6f7674041'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# allowsMagnification

<sub>Instance Property</sub>

A Boolean value that indicates whether the magnify gesture changes the video’s view magnification.

<sub>macOS</sub>

```swift
var allowsMagnification: Bool { get set }
```

## Discussion

The default value is `false`. This property only affects whether the magnify gesture triggers magnification. Your app can still programmatically change magnification even when the value of this is `false`, which matches the behavior of [NSScrollView](../../appkit/nsscrollview.md).

## See Also

### Magnifying video

- [magnification](magnification.md) — The factor by which the video’s view is currently scaled.
- [- setMagnification:centeredAtPoint:](<setmagnification(__centeredat_).md>) — Scales the video’s view by a specified factor, and centers the result on a specified point.
