---
title: 'pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback%28_%3A%29.json'
content_hash: 'sha256:5e818109bdffc017'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(_:)

<sub>Instance Method</sub>

Asks the delegate whether to always prohibit background audio playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureControllerShouldProhibitBackgroundAudioPlayback(_ pictureInPictureController: AVPictureInPictureController) -> Bool
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller instance.

## Return Value

`true` if the delegate prohibits background audio playback; otherwise, `false`.

## Discussion

If you implement this method, the system calls it once for each invocation of [- invalidatePlaybackState](<../avpictureinpicturecontroller/invalidateplaybackstate().md>) to determine whether to prohibit audio playback when the Picture in Picture window is in the background.

## See Also

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerTimeRangeForPlayback:](<pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureControllerIsPlaybackPaused:](<pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:didTransitionToRenderSize:](<pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureController:skipByInterval:completionHandler:](<pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
