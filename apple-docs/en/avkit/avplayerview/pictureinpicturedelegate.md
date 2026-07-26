---
title: pictureInPictureDelegate
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/pictureinpicturedelegate
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/pictureinpicturedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/pictureinpicturedelegate.json'
content_hash: 'sha256:09a890249244e5fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# pictureInPictureDelegate

<sub>Instance Property</sub>

The Picture in Picture delegate object.

<sub>macOS</sub>

```swift
weak var pictureInPictureDelegate: (any AVPlayerViewPictureInPictureDelegate)? { get set }
```

## See Also

### Configuring picture in picture

- [allowsPictureInPicturePlayback](allowspictureinpictureplayback.md) — A Boolean value that determines whether the player view allows Picture in Picture playback.
- [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md) — A protocol that defines the methods to implement to respond to Picture in Picture playback events.
