---
title: AVLayerVideoGravity
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avlayervideogravity
source_url: 'https://developer.apple.com/documentation/avfoundation/avlayervideogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avlayervideogravity.json'
content_hash: 'sha256:300e07bf8f9b5396'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVLayerVideoGravity

<sub>Structure</sub>

A structure that defines how a layer displays a player’s visual content within the layer’s bounds.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVLayerVideoGravity
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Video gravities

- [AVLayerVideoGravityResize](avlayervideogravity/resize.md) — The video stretches to fill the layer’s bounds.
- [AVLayerVideoGravityResizeAspect](avlayervideogravity/resizeaspect.md) — The video preserves its aspect ratio and fits it within the layer’s bounds.
- [AVLayerVideoGravityResizeAspectFill](avlayervideogravity/resizeaspectfill.md) — The video preserves its aspect ratio and fills the layer’s bounds.

### Initializers

- [init(rawValue:)](<avlayervideogravity/init(rawvalue_).md>) — Creates a video gravity with a string value.

## See Also

### Configuring the presentation

- [videoRect](avplayerlayer/videorect.md) — The current size and position of the video image that displays within the layer’s bounds.
- [videoGravity](avplayerlayer/videogravity.md) — A value that specifies how the layer displays the player’s visual content within the layer’s bounds.
