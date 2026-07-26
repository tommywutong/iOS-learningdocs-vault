---
title: allowsPictureInPicturePlayback
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/allowspictureinpictureplayback
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/allowspictureinpictureplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/allowspictureinpictureplayback.json'
content_hash: 'sha256:9b053481bd145899'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# allowsPictureInPicturePlayback

<sub>Instance Property</sub>

A Boolean value that determines whether the player view allows Picture in Picture playback.

<sub>macOS</sub>

```swift
var allowsPictureInPicturePlayback: Bool { get set }
```

## Discussion

The default value is `false`.

## See Also

### Configuring picture in picture

- [pictureInPictureDelegate](pictureinpicturedelegate.md) — The Picture in Picture delegate object.
- [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md) — A protocol that defines the methods to implement to respond to Picture in Picture playback events.
