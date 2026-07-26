---
title: noItemToPlay
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/waitingreason/noitemtoplay
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/noitemtoplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/waitingreason/noitemtoplay.json'
content_hash: 'sha256:8294effc560b017e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [WaitingReason](../waitingreason.md)

# noItemToPlay

<sub>Type Property</sub>

The player is waiting because there’s no item to play.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let noItemToPlay: AVPlayer.WaitingReason
```

## See Also

### Player waiting reasons

- [AVPlayerWaitingWhileEvaluatingBufferingRateReason](evaluatingbufferingrate.md) — The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.
- [AVPlayerWaitingToMinimizeStallsReason](tominimizestalls.md) — The player is waiting for appropriate playback conditions before starting playback.
- [AVPlayerWaitingDuringInterstitialEventReason](interstitialevent.md) — The player is waiting for an interstitial event to complete.
- [AVPlayerWaitingForCoordinatedPlaybackReason](waitingforcoordinatedplayback.md) — The player is waiting for another participant in a coordinated playback session.
