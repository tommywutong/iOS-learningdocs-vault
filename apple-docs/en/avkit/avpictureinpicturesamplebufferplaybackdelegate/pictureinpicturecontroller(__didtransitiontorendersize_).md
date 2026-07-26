---
title: 'pictureInPictureController(_:didTransitionToRenderSize:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:didtransitiontorendersize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_%3Adidtransitiontorendersize%3A%29.json'
content_hash: 'sha256:5b695ab6f012a53a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureController(_:didTransitionToRenderSize:)

<sub>Instance Method</sub>

Tells the delegate when the system Picture in Picture window changes size.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, didTransitionToRenderSize newRenderSize: CMVideoDimensions)
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller.

- `newRenderSize` — The Picture in Picture content’s rendered size, in pixels.

## Discussion

Take the new render size and the [pictureInPictureActive](../avpictureinpicturecontroller/ispictureinpictureactive.md) state into account when choosing media variants to avoid uncessary decoding overhead.

## See Also

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerTimeRangeForPlayback:](<pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureControllerIsPlaybackPaused:](<pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:skipByInterval:completionHandler:](<pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.
