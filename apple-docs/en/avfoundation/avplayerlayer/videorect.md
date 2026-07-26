---
title: videoRect
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlayer/videorect
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/videorect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/videorect.json'
content_hash: 'sha256:11603c4b7ef89fa6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# videoRect

<sub>Instance Property</sub>

The current size and position of the video image that displays within the layer’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var videoRect: CGRect { get }
```

## Discussion

The size and position of a rectangle depends on the aspect ratio of the media (16:9 or 4:3), the layer’s [bounds](../../quartzcore/calayer/bounds.md), and the value of its [videoGravity](videogravity.md) property.

This property is key-value observable.

## See Also

### Configuring the presentation

- [videoGravity](videogravity.md) — A value that specifies how the layer displays the player’s visual content within the layer’s bounds.
- [AVLayerVideoGravity](../avlayervideogravity.md) — A structure that defines how a layer displays a player’s visual content within the layer’s bounds.
