---
title: AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.json'
content_hash: 'sha256:4516d3855d582458'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [TimeControlStatus](../timecontrolstatus-swift.enum.md)

# AVPlayer.TimeControlStatus.waitingToPlayAtSpecifiedRate

<sub>Case</sub>

A state that indicates that the player is waiting for network conditions to improve before it can start or resume playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case waitingToPlayAtSpecifiedRate
```

## Discussion

The player enters this state in the following conditions:

- Playback stalls because the playback buffer is empty.
- The playback rate changes from zero to a nonzero value and there isn’t enough media to start playback.
- The value of its [currentItem](../currentitem.md) property is `nil`.

In this state, the value of the [rate](../rate.md) property doesn’t indicate the current playback rate, but the rate at which playback starts or resumes. Refer to the value of [reasonForWaitingToPlay](../reasonforwaitingtoplay.md) for details about the player is waiting and the conditions that allow its status to change to [AVPlayerTimeControlStatusPlaying](playing.md).

> [!tip] Tip
> While waiting for buffering, you can attempt to start playback of any available media data by calling [- playImmediatelyAtRate:](<../playimmediately(atrate_).md>).

## See Also

### Status values

- [AVPlayerTimeControlStatusPaused](paused.md) — A state that indicates the player paused playback indefinitely.
- [AVPlayerTimeControlStatusPlaying](playing.md) — A state that indicates that the player is currently playing media.
