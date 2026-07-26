---
title: 'pictureInPictureControllerIsPlaybackPaused(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused%28_%3A%29.json'
content_hash: 'sha256:71ec755c0aafbc29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureControllerIsPlaybackPaused(_:)

<sub>Instance Method</sub>

Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureControllerIsPlaybackPaused(_ pictureInPictureController: AVPictureInPictureController) -> Bool
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller.

## Return Value

`true` to indicate a paused state, otherwise `false`.

## Discussion

The system calls this method whenever you call its [- invalidatePlaybackState](<../avpictureinpicturecontroller/invalidateplaybackstate().md>) method, and at other times as it requires.

## See Also

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerTimeRangeForPlayback:](<pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureController:didTransitionToRenderSize:](<pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureController:skipByInterval:completionHandler:](<pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.
