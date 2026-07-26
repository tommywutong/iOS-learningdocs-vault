---
title: 'playImmediately(atRate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/playimmediately(atrate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/playimmediately(atrate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/playimmediately%28atrate%3A%29.json'
content_hash: 'sha256:02503e0382ef5bae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# playImmediately(atRate:)

<sub>Instance Method</sub>

Plays the available media data immediately, at the specified rate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func playImmediately(atRate rate: Float)
```

## Parameters

- `rate` — The specified playback rate.

## Discussion

This method plays the available media data at the specified `rate` regardless of whether there is sufficient media buffered to ensure smooth playback. If media data exists in the playback buffer, calling this method changes the player’s playback rate to the specified `rate` and its [timeControlStatus](timecontrolstatus-swift.property.md) to a value of [AVPlayerTimeControlStatusPlaying](timecontrolstatus-swift.enum/playing.md). If the player has insufficient media data buffered to begin playback, the player will behave as if it has encountered a stall during playback, except that no [AVPlayerItemPlaybackStalledNotification](../avplayeritem/playbackstallednotification.md) will be posted.

## See Also

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [reasonForWaitingToPlay](reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [WaitingReason](waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [timeControlStatus](timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [TimeControlStatus](timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
