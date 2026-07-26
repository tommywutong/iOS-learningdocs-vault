---
title: 'pictureInPictureController(_:setPlaying:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:setplaying:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:setplaying:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_%3Asetplaying%3A%29.json'
content_hash: 'sha256:cb34144ae4e5246d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureController(_:setPlaying:)

<sub>Instance Method</sub>

Tells the delegate that the user requested to begin or pause playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, setPlaying playing: Bool)
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller.

- `playing` — A Boolean value that indicates whether to begin or pause playback.

## See Also

### Responding to Playback Events

- [- pictureInPictureControllerTimeRangeForPlayback:](<pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureControllerIsPlaybackPaused:](<pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:didTransitionToRenderSize:](<pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureController:skipByInterval:completionHandler:](<pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.
