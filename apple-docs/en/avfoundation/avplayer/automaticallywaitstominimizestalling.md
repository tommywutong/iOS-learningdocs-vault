---
title: automaticallyWaitsToMinimizeStalling
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/automaticallywaitstominimizestalling
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/automaticallywaitstominimizestalling'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/automaticallywaitstominimizestalling.json'
content_hash: 'sha256:46f657c4e98a6b27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# automaticallyWaitsToMinimizeStalling

<sub>Instance Property</sub>

A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var automaticallyWaitsToMinimizeStalling: Bool { get set }
```

## Discussion

When playing media delivered over HTTP, this property is used to determine if the player should automatically delay playback in order to minimize stalling. When this property is [true](../../swift/true.md) and the player changes from a paused state ([rate](rate.md) of `0.0`) to a played state ([rate](rate.md) \> `0.0`), the player will try to determine if the current item can play to its end at the currently specified rate. If it determines that it’s likely to encounter a stall, the value of the player’s [timeControlStatus](timecontrolstatus-swift.property.md) will change to [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) and playback will automatically start when the likelihood of stalling has been minimized. A similar condition will occur during playback if the current player item’s playback buffer is exhausted and playback stalls. Playback will automatically resume when the likelihood of stalling has been minimized.

You will need to set this property to [false](../../swift/false.md) when you require precise control over playback start times, such as if you’re are synchronizing multiple player instances using the [- setRate:time:atHostTime:](<setrate(__time_athosttime_).md>) method. If the value of this property is [false](../../swift/false.md), playback will start immediately when requested as long as the playback buffer is not empty. If the playback buffer becomes empty and playback stalls, the player’s [timeControlStatus](timecontrolstatus-swift.property.md) will switch to [AVPlayerTimeControlStatusPaused](timecontrolstatus-swift.enum/paused.md) and the playback rate will change to `0.0`.

Changing the value of this property to [false](../../swift/false.md) while the player’s [timeControlStatus](timecontrolstatus-swift.property.md) is [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) and its [reasonForWaitingToPlay](reasonforwaitingtoplay.md) is [AVPlayerWaitingToMinimizeStallsReason](waitingreason/tominimizestalls.md) will cause the player to immediately attempt playback at the specified rate.

> [!important] Important
> For clients linked against iOS 10.0 and later or macOS 10.12 and later (and running on those versions), the default value of this property is [true](../../swift/true.md). This property did not exist in previous OS versions and the observed behavior was dependent on the type of media played:
>
> - **HTTP Live Streaming (HLS):** When playing HLS media, the player behaved as if [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) is [true](../../swift/true.md).
> - **File-based Media:** When playing file-based media, including progressively downloaded content, the player behaved as if [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) is [false](../../swift/false.md).
>
> You should verify that your playback applications perform as expected using this new default automatic waiting behavior.

## See Also

### Configuring waiting behavior

- [reasonForWaitingToPlay](reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [WaitingReason](waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [timeControlStatus](timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [TimeControlStatus](timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
- [- playImmediatelyAtRate:](<playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.
