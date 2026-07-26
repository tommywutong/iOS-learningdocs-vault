---
title: playerLayer
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/playerlayer
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/playerlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/playerlayer.json'
content_hash: 'sha256:94dce408a9fea8a7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# playerLayer

<sub>Instance Property</sub>

The presenting player layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var playerLayer: AVPlayerLayer? { get }
```

## Discussion

This value is `nil` if the content source doesn’t represent a player layer.

## See Also

### Accessing the Presentation Layer

- [sampleBufferDisplayLayer](samplebufferdisplaylayer.md) — The presenting sample buffer display layer.
