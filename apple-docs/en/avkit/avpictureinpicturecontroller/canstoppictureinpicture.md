---
title: canStopPictureInPicture
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/canstoppictureinpicture
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/canstoppictureinpicture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/canstoppictureinpicture.json'
content_hash: 'sha256:2793cf9170374ff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# canStopPictureInPicture

<sub>Instance Property</sub>

A Boolean value that indicates whether Picture in Picture is active and is able to stop.

<sub>tvOS</sub>

```swift
var canStopPictureInPicture: Bool { get }
```

## Discussion

When this value is `true`, calling [- stopPictureInPicture](<stoppictureinpicture().md>) stops the active Picture in Picture session. Apps should update the state of UI that starts Picture in Picture when this property value changes.

Thie value is key-value observable.

## See Also

### Controlling Picture in Picture Playback

- [canStartPictureInPictureAutomaticallyFromInline](canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [- startPictureInPicture](<startpictureinpicture().md>) — Starts Picture in Picture, if possible.
- [- stopPictureInPicture](<stoppictureinpicture().md>) — Stops Picture in Picture, if active.
- [- invalidatePlaybackState](<invalidateplaybackstate().md>) — Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.
