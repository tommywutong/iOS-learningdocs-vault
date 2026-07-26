---
title: allowsPictureInPicturePlayback
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/allowspictureinpictureplayback
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/allowspictureinpictureplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/allowspictureinpictureplayback.json'
content_hash: 'sha256:70e33e07d30b0e31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# allowsPictureInPicturePlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the player allows Picture in Picture playback.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var allowsPictureInPicturePlayback: Bool { get set }
```

## Discussion

Set this value to `false` to disable Picture in Picture playback. The default value is `true`.

## See Also

### Configuring Picture in Picture

- [canStartPictureInPictureAutomaticallyFromInline](canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when transitioning to the background when the view controller presents its content inline.
