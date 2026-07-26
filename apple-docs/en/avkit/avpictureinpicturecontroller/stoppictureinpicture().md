---
title: stopPictureInPicture()
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/stoppictureinpicture()
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/stoppictureinpicture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/stoppictureinpicture%28%29.json'
content_hash: 'sha256:aa35fe176956b929'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# stopPictureInPicture()

<sub>Instance Method</sub>

Stops Picture in Picture, if active.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func stopPictureInPicture()
```

## Discussion

Regardless of how Picture in Picture stops, the controller calls the delegate’s [- pictureInPictureControllerWillStopPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(__).md>) method. When the PiP animation completes, the controller finalizes the session by calling the delegate’s [- pictureInPictureControllerDidStopPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(__).md>) method.

## See Also

### Controlling Picture in Picture Playback

- [canStopPictureInPicture](canstoppictureinpicture.md) — A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [canStartPictureInPictureAutomaticallyFromInline](canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [- startPictureInPicture](<startpictureinpicture().md>) — Starts Picture in Picture, if possible.
- [- invalidatePlaybackState](<invalidateplaybackstate().md>) — Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.
