---
title: videoGravity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/videogravity
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/videogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/videogravity.json'
content_hash: 'sha256:cfac1032a6793cfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# videoGravity

<sub>Instance Property</sub>

A value that indicates how the layer displays video within its bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoGravity: AVLayerVideoGravity { get set }
```

## Discussion

[AVLayerVideoGravity](../avlayervideogravity.md) defines the supported video gravities. The default value is [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md).

## See Also

### Configuring the layer

- [readyForDisplay](isreadyfordisplay.md) — A Boolean value that indicates whether the first video frame is ready for display.
- [controlTimebase](controltimebase.md) — A timebase that determines how the layer interprets timestamps.
- [AVLayerVideoGravity](../avlayervideogravity.md) — A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
