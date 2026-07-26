---
title: videoGravity
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/videogravity
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/videogravity.json'
content_hash: 'sha256:a7c89953ec83f9b4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# videoGravity

<sub>Instance Property</sub>

A value that determines how the player view displays video content within its bounds.

<sub>macOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

The video gravity determines how the player view scales or stretches the video content within the player view’s bounds. The player view supports the following video gravity values:

- [resizeAspect](../../avfoundation/avlayervideogravity/resizeaspect.md)
- [resizeAspectFill](../../avfoundation/avlayervideogravity/resizeaspectfill.md)
- [resize](../../avfoundation/avlayervideogravity/resize.md)

The default value is [resizeAspect](../../avfoundation/avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

### Customizing the video presentation

- [readyForDisplay](isreadyfordisplay.md) — A Boolean value that indicates whether the current player item’s first video frame is ready for display.
- [videoBounds](videobounds.md) — The current size and position of the video image that displays within the player view’s bounds.
