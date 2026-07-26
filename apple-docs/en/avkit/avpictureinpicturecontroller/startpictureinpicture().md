---
title: startPictureInPicture()
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/startpictureinpicture()
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/startpictureinpicture()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/startpictureinpicture%28%29.json'
content_hash: 'sha256:1da4cc626625f302'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# startPictureInPicture()

<sub>Instance Method</sub>

Starts Picture in Picture, if possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func startPictureInPicture()
```

## Discussion

When you call this method and Picture in Picture (PiP) is possible, your delegate receives a call to its [- pictureInPictureControllerWillStartPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstartpictureinpicture(__).md>) method. After a successful start, your delegate receives a call to the [- pictureInPictureControllerDidStartPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(__).md>) method.

If PiP fails, your delegate receives a call to the [- pictureInPictureController:failedToStartPictureInPictureWithError:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(__failedtostartpictureinpicturewitherror_).md>)method.

Whether you explicitly stop PiP, the user stops it through interaction, or the system stops it, your delegate receives a call to the [- pictureInPictureControllerWillStopPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(__).md>) method, followed by the [- pictureInPictureControllerDidStopPictureInPicture:](<../avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstoppictureinpicture(__).md>) method after the PiP stop animation completes.

## See Also

### Controlling Picture in Picture Playback

- [canStopPictureInPicture](canstoppictureinpicture.md) — A Boolean value that indicates whether Picture in Picture is active and is able to stop.
- [canStartPictureInPictureAutomaticallyFromInline](canstartpictureinpictureautomaticallyfrominline.md) — A Boolean value that indicates whether Picture in Picture starts automatically when the controller embeds its content inline and the app transitions to the background.
- [- stopPictureInPicture](<stoppictureinpicture().md>) — Stops Picture in Picture, if active.
- [- invalidatePlaybackState](<invalidateplaybackstate().md>) — Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.
