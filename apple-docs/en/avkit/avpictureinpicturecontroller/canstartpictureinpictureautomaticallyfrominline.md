---
title: canStartPictureInPictureAutomaticallyFromInline
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.2+, iPadOS 14.2+, Mac Catalyst 14.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/canstartpictureinpictureautomaticallyfrominline.json'
content_hash: 'sha256:77d053f1ddcc22e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# canStartPictureInPictureAutomaticallyFromInline

<sub>Instance Property</sub>

A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var canStartPictureInPictureAutomaticallyFromInline: Bool { get set }
```

## Discussion

Only set this value to `true` for content that you intend to be the user’s primary focus.

## See Also

### Controlling Picture in Picture Playback

- [canStopPictureInPicture](canstoppictureinpicture.md) — A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [- startPictureInPicture](<startpictureinpicture().md>) — Starts Picture in Picture, if possible.
- [- stopPictureInPicture](<stoppictureinpicture().md>) — Stops Picture in Picture, if active.
- [- invalidatePlaybackState](<invalidateplaybackstate().md>) — Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.
