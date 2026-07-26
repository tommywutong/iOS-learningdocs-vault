---
title: 'pictureInPictureControllerTimeRangeForPlayback(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback%28_%3A%29.json'
content_hash: 'sha256:a5559a894babc658'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureControllerTimeRangeForPlayback(_:)

<sub>Instance Method</sub>

Asks the delegate for the current playable time range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureControllerTimeRangeForPlayback(_ pictureInPictureController: AVPictureInPictureController) -> CMTimeRange
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller.

## Return Value

A [CMTimeRange](../../coremedia/cmtimerange.md) value that defines the content’s time range.

## Discussion

Use the following guidelines when specifying a time range value:

- For live content, return a time range with a duration of [positiveInfinity](../../coremedia/cmtime/positiveinfinity.md).
- For nonlive content, return a time range that contains the current time of the sample buffer display layer’s timebase.
- When there’s no content to play, return [invalid](../../coremedia/cmtimerange/invalid.md).

The system calls this method whenever you call the [- invalidatePlaybackState](<../avpictureinpicturecontroller/invalidateplaybackstate().md>) method, and at other times as it requires.

## See Also

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerIsPlaybackPaused:](<pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:didTransitionToRenderSize:](<pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureController:skipByInterval:completionHandler:](<pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.
