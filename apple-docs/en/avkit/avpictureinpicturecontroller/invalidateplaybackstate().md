---
title: invalidatePlaybackState()
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/invalidateplaybackstate()
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/invalidateplaybackstate()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/invalidateplaybackstate%28%29.json'
content_hash: 'sha256:dd8a2b8532a17cf8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# invalidatePlaybackState()

<sub>Instance Method</sub>

Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func invalidatePlaybackState()
```

## Discussion

Call this method whenever you start or pause playback and when the underlying content duration changes.

## See Also

### Controlling Picture in Picture Playback

- [canStopPictureInPicture](canstoppictureinpicture.md) — A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [canStartPictureInPictureAutomaticallyFromInline](canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [- startPictureInPicture](<startpictureinpicture().md>) — Starts Picture in Picture, if possible.
- [- stopPictureInPicture](<stoppictureinpicture().md>) — Stops Picture in Picture, if active.
