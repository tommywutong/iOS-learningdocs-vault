---
title: toMinimizeStalls
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/waitingreason/tominimizestalls
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/tominimizestalls'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/waitingreason/tominimizestalls.json'
content_hash: 'sha256:e77cc1674bf1ada8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [WaitingReason](../waitingreason.md)

# toMinimizeStalls

<sub>Type Property</sub>

The player is waiting for appropriate playback conditions before starting playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let toMinimizeStalls: AVPlayer.WaitingReason
```

## Discussion

Playback continues at the specified rate when conditions allow playback to begin without stalling. Playback also continues if the player item’s playback buffer is full and no further buffering of media data is possible.

## See Also

### Player waiting reasons

- [AVPlayerWaitingWhileEvaluatingBufferingRateReason](evaluatingbufferingrate.md) — The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [AVPlayerWaitingWithNoItemToPlayReason](noitemtoplay.md) — The player is waiting because there’s no item to play.
- [AVPlayerWaitingDuringInterstitialEventReason](interstitialevent.md) — The player is waiting for an interstitial event to complete.
- [AVPlayerWaitingForCoordinatedPlaybackReason](waitingforcoordinatedplayback.md) — The player is waiting for another participant in a coordinated playback session.
