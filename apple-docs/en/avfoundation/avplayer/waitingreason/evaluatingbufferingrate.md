---
title: evaluatingBufferingRate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/waitingreason/evaluatingbufferingrate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/waitingreason/evaluatingbufferingrate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/waitingreason/evaluatingbufferingrate.json'
content_hash: 'sha256:69e646d8687147aa'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [WaitingReason](../waitingreason.md)

# evaluatingBufferingRate

<sub>Type Property</sub>

The player is waiting because it’s monitoring the buffer’s fill rate to determine whether playback is likely to complete without interruptions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let evaluatingBufferingRate: AVPlayer.WaitingReason
```

## See Also

### Player waiting reasons

- [AVPlayerWaitingWithNoItemToPlayReason](noitemtoplay.md) — The player is waiting because there’s no item to play.
- [AVPlayerWaitingToMinimizeStallsReason](tominimizestalls.md) — The player is waiting for appropriate playback conditions before starting playback.
- [AVPlayerWaitingDuringInterstitialEventReason](interstitialevent.md) — The player is waiting for an interstitial event to complete.
- [AVPlayerWaitingForCoordinatedPlaybackReason](waitingforcoordinatedplayback.md) — The player is waiting for another participant in a coordinated playback session.
