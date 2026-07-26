---
title: waitingForCoordinatedPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/waitingreason/waitingforcoordinatedplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/waitingforcoordinatedplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/waitingreason/waitingforcoordinatedplayback.json'
content_hash: 'sha256:29ca52aadb6a148f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [WaitingReason](../waitingreason.md)

# waitingForCoordinatedPlayback

<sub>Type Property</sub>

The player is waiting for another participant in a coordinated playback session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let waitingForCoordinatedPlayback: AVPlayer.WaitingReason
```

## See Also

### Player waiting reasons

- [AVPlayerWaitingWhileEvaluatingBufferingRateReason](evaluatingbufferingrate.md) — The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [AVPlayerWaitingWithNoItemToPlayReason](noitemtoplay.md) — The player is waiting because there’s no item to play.
- [AVPlayerWaitingToMinimizeStallsReason](tominimizestalls.md) — The player is waiting for appropriate playback conditions before starting playback.
- [AVPlayerWaitingDuringInterstitialEventReason](interstitialevent.md) — The player is waiting for an interstitial event to complete.
