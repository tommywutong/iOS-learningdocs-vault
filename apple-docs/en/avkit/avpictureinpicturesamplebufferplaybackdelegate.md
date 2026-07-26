---
title: AVPictureInPictureSampleBufferPlaybackDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturesamplebufferplaybackdelegate.json'
content_hash: 'sha256:e91cf6fb1e55d354'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPictureInPictureSampleBufferPlaybackDelegate

<sub>Protocol</sub>

A protocol for controlling playback from a sample buffer display layer in Picture in Picture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVPictureInPictureSampleBufferPlaybackDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Playback Events

- [- pictureInPictureController:setPlaying:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(__setplaying_).md>) — Tells the delegate that the user requested to begin or pause playback.
- [- pictureInPictureControllerTimeRangeForPlayback:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollertimerangeforplayback(__).md>) — Asks the delegate for the current playable time range.
- [- pictureInPictureControllerIsPlaybackPaused:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollerisplaybackpaused(__).md>) — Asks delegate to indicate whether the playback UI reflects a playing or paused state, regardless of the current playback rate.
- [- pictureInPictureController:didTransitionToRenderSize:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(__didtransitiontorendersize_).md>) — Tells the delegate when the system Picture in Picture window changes size.
- [- pictureInPictureController:skipByInterval:completionHandler:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontroller(__skipbyinterval_completion_).md>) — Tells the delegate that the user has requested skipping forward or backward by the indicated time interval.
- [- pictureInPictureControllerShouldProhibitBackgroundAudioPlayback:](<avpictureinpicturesamplebufferplaybackdelegate/pictureinpicturecontrollershouldprohibitbackgroundaudioplayback(__).md>) — Asks the delegate whether to always prohibit background audio playback.

## See Also

### Configuring the Delegate

- [sampleBufferPlaybackDelegate](avpictureinpicturecontroller/contentsource-swift.class/samplebufferplaybackdelegate.md) — A delegate object that responds to sample buffer playback events.
