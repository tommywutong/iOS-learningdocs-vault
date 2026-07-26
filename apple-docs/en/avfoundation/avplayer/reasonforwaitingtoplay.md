---
title: reasonForWaitingToPlay
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/reasonforwaitingtoplay
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/reasonforwaitingtoplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/reasonforwaitingtoplay.json'
content_hash: 'sha256:658e348f2183c9ec'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# reasonForWaitingToPlay

<sub>Instance Property</sub>

The reason the player is currently waiting for playback to begin or resume.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var reasonForWaitingToPlay: AVPlayer.WaitingReason? { get }
```

## Discussion

When the value of the player’s [timeControlStatus](timecontrolstatus-swift.property.md) is [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md), you can use this property determine the reason the player is currently waiting for playback to begin or resume. Possible values for this property are:

- [AVPlayerWaitingToMinimizeStallsReason](waitingreason/tominimizestalls.md)
- [AVPlayerWaitingWithNoItemToPlayReason](waitingreason/noitemtoplay.md)
- [AVPlayerWaitingWhileEvaluatingBufferingRateReason](waitingreason/evaluatingbufferingrate.md)

The value of this property will be `nil` if the player’s [timeControlStatus](timecontrolstatus-swift.property.md) is a value other than [AVPlayerTimeControlStatusWaitingToPlayAtSpecifiedRate](timecontrolstatus-swift.enum/waitingtoplayatspecifiedrate.md).

You can use the value of this property to conditionally show UI indicating the player’s waiting state. This property is observable using key-value observing.

## See Also

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [WaitingReason](waitingreason.md) — The reasons a player is waiting to begin or resume playback.
- [timeControlStatus](timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [TimeControlStatus](timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
- [- playImmediatelyAtRate:](<playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.
