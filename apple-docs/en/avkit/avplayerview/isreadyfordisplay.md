---
title: isReadyForDisplay
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/isreadyfordisplay
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/isreadyfordisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/isreadyfordisplay.json'
content_hash: 'sha256:2a6b9b4c73e1f54c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# isReadyForDisplay

<sub>Instance Property</sub>

A Boolean value that indicates whether the current player item’s first video frame is ready for display.

<sub>macOS</sub>

```swift
var isReadyForDisplay: Bool { get }
```

## Discussion

This property value is key-value observable.

## See Also

### Customizing the video presentation

- [videoBounds](videobounds.md) — The current size and position of the video image that displays within the player view’s bounds.
- [videoGravity](videogravity.md) — A value that determines how the player view displays video content within its bounds.
