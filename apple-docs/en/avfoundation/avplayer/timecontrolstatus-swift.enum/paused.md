---
title: AVPlayer.TimeControlStatus.paused
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/paused
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/paused'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/paused.json'
content_hash: 'sha256:e8c5327aa823d402'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [TimeControlStatus](../timecontrolstatus-swift.enum.md)

# AVPlayer.TimeControlStatus.paused

<sub>Case</sub>

A state that indicates the player paused playback indefinitely.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case paused
```

## Discussion

In this state, the player pauses indefinitely and doesn’t resume playback until you call its play method. You can also resume playback if the player has sufficent data to start playback by calling the player’s [- setRate:time:atHostTime:](<../setrate(__time_athosttime_).md>) or [- playImmediatelyAtRate:](<../playimmediately(atrate_).md>) method with a nonzero rate value.

## See Also

### Status values

- [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](waitingtoplayatspecifiedrate.md) — A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.
- [AVPlayerTimeControlStatusPlaying](playing.md) — A state that indicates that the player is currently playing media.
