---
title: AVPlayer.WaitingReason
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/waitingreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/waitingreason.json'
content_hash: 'sha256:bb488db96861f0e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.WaitingReason

<sub>Structure</sub>

The reasons a player is waiting to begin or resume playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct WaitingReason
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Player waiting reasons

- [AVPlayerWaitingWhileEvaluatingBufferingRateReason](waitingreason/evaluatingbufferingrate.md) — The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [AVPlayerWaitingWithNoItemToPlayReason](waitingreason/noitemtoplay.md) — The player is waiting because there’s no item to play.
- [AVPlayerWaitingToMinimizeStallsReason](waitingreason/tominimizestalls.md) — The player is waiting for appropriate playback conditions before starting playback.
- [AVPlayerWaitingDuringInterstitialEventReason](waitingreason/interstitialevent.md) — The player is waiting for an interstitial event to complete.
- [AVPlayerWaitingForCoordinatedPlaybackReason](waitingreason/waitingforcoordinatedplayback.md) — The player is waiting for another participant in a coordinated playback session.

### Initializers

- [init(rawValue:)](<waitingreason/init(rawvalue_).md>) — Creates a waiting reason with a string value.

## See Also

### Configuring waiting behavior

- [automaticallyWaitsToMinimizeStalling](automaticallywaitstominimizestalling.md) — A Boolean value that indicates whether the player should automatically delay playback in order to minimize stalling.
- [reasonForWaitingToPlay](reasonforwaitingtoplay.md) — The reason the player is currently waiting for playback to begin or resume.
- [timeControlStatus](timecontrolstatus-swift.property.md) — A value that indicates whether playback is in progress, paused indefinitely, or waiting for network conditions to improve.
- [TimeControlStatus](timecontrolstatus-swift.enum.md) — Constants that indicate the state of playback control.
- [- playImmediatelyAtRate:](<playimmediately(atrate_).md>) — Plays the available media data immediately, at the specified rate.
