---
title: videoGravity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlayer/videogravity
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/videogravity.json'
content_hash: 'sha256:17151fe5da79e386'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# videoGravity

<sub>Instance Property</sub>

A value that specifies how the layer displays the player’s visual content within the layer’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

A player layer supports the following video gravity values:

- [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md)
- [AVLayerVideoGravityResizeAspectFill](../avlayervideogravity/resizeaspectfill.md)
- [AVLayerVideoGravityResize](../avlayervideogravity/resize.md)

The default value is [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md).

This property is animatable.

## See Also

### Configuring the presentation

- [videoRect](videorect.md) — The current size and position of the video image that displays within the layer’s bounds.
- [AVLayerVideoGravity](../avlayervideogravity.md) — A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
