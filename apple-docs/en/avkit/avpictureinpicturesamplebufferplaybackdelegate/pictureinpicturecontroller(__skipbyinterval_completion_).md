---
title: 'pictureInPictureController(_:skipByInterval:completion:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(_:skipbyinterval:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller%28_%3Askipbyinterval%3Acompletion%3A%29.json'
content_hash: 'sha256:f2ec12a125a29de5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md)

# pictureInPictureController(_:skipByInterval:completion:)

<sub>Instance Method</sub>

Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime, completion completionHandler: @escaping @Sendable () -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, skipByInterval skipInterval: CMTime) async
```

## Parameters

- `pictureInPictureController` — The Picture in Picture controller.

- `skipInterval` — A [CMTime](../../coremedia/cmtime.md) value that indicates the time interval by which to skip.

- `completionHandler` — You must call the completion handler whether your seek operation succeeds or fails. Failing to call the completion handler is an app error and leaves the user interface in a seeking state.

## Discussion

Your app’s implementation of this method may choose to seek by a different interval for efficiency reasons, such as seeking to a particular key frame or only allowing seeks that fall within the playable timeline.

> [!important] Important
> Before calling the completion handler, ensure the seek operation is complete and the timebase reflects the current time and playback rate.

## See Also

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerTimeRangeForPlayback:](<pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureControllerIsPlaybackPaused:](<pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:didTransitionToRenderSize:](<pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.
