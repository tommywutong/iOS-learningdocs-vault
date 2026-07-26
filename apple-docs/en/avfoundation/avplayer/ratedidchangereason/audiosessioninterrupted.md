---
title: audioSessionInterrupted
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/ratedidchangereason/audiosessioninterrupted
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/ratedidchangereason/audiosessioninterrupted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/ratedidchangereason/audiosessioninterrupted.json'
content_hash: 'sha256:940e87a1e28b5636'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [RateDidChangeReason](../ratedidchangereason.md)

# audioSessionInterrupted

<sub>Type Property</sub>

The system interrupts the app’s audio session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let audioSessionInterrupted: AVPlayer.RateDidChangeReason
```

## See Also

### Rate change reasons

- [AVPlayerRateDidChangeReasonAppBackgrounded](appbackgrounded.md) — An app transitions to the background.
- [AVPlayerRateDidChangeReasonSetRateCalled](setratecalled.md) — An app makes a call to set the player’s rate.
- [AVPlayerRateDidChangeReasonSetRateFailed](setratefailed.md) — An attempt to change the player’s rate fails.
