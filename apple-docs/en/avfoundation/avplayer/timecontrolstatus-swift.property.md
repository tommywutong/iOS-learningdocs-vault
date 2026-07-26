---
title: timeControlStatus
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/timecontrolstatus-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/timecontrolstatus-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/timecontrolstatus-swift.property.json'
content_hash: 'sha256:dc29ad1b3695daaa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# timeControlStatus

<sub>Instance Property</sub>

A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var timeControlStatus: AVPlayer.TimeControlStatus { get }
```

## Discussion

When the value of [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) is [true](../../swift/true.md), the player waits until your app resumes playback.

During playback, the value of the property changes between [AVPlayerTimeControlStatusPlaying](timecontrolstatus-swift.enum/playing.md) and [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md) depending on whether the player has sufficient media data to continue playback.

This property is key-value observable.

## See Also

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [reasonForWaitingToPlay](reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [WaitingReason](waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [TimeControlStatus](timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
- [- playImmediatelyAtRate:](<playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.
