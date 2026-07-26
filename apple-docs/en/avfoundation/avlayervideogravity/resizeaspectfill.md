---
title: resizeAspectFill
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avlayervideogravity/resizeaspectfill
source_url: 'https://developer.apple.com/documentation/avfoundation/avlayervideogravity/resizeaspectfill'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avlayervideogravity/resizeaspectfill.json'
content_hash: 'sha256:a33e8f7621fc423c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVLayerVideoGravity](../avlayervideogravity.md)

# resizeAspectFill

<sub>Type Property</sub>

The video preserves its aspect ratio and fills the layer’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let resizeAspectFill: AVLayerVideoGravity
```

## Discussion

This gravity value may crop the video image along its horizontal or vertical dimension.

## See Also

### Video gravities

- [AVLayerVideoGravityResize](resize.md) — The video stretches to fill the layer’s bounds.
- [AVLayerVideoGravityResizeAspect](resizeaspect.md) — The video preserves its aspect ratio and fits it within the layer’s bounds.
