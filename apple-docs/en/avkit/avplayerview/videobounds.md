---
title: videoBounds
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/videobounds
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/videobounds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/videobounds.json'
content_hash: 'sha256:ed7d3f7c6dc3cced'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# videoBounds

<sub>Instance Property</sub>

The current size and position of the video image that displays within the player view’s bounds.

<sub>macOS</sub>

```swift
var videoBounds: NSRect { get }
```

## Discussion

Use this property to determine the display dimensions of the video image within the player view’s bounds. The size and position of this rectangle depend on the aspect ratio of the media (like 16:9 or 4:3), the player view’s [bounds](../../appkit/nsview/bounds.md), and its [controlsStyle](controlsstyle.md).

## See Also

### Customizing the video presentation

- [readyForDisplay](isreadyfordisplay.md) — A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [videoGravity](videogravity.md) — A value that determines how the player view displays video content within its bounds.
