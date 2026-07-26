---
title: requiresPlaybackAtPreferredRateForAdvancement
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.json'
content_hash: 'sha256:f8258b76ce56c26f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayerInterstitialEvent](../../avplayerinterstitialevent.md) · [Restrictions](../restrictions-swift.struct.md)

# requiresPlaybackAtPreferredRateForAdvancement

<sub>Type Property</sub>

A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var requiresPlaybackAtPreferredRateForAdvancement: AVPlayerInterstitialEvent.Restrictions { get }
```

## See Also

### Configure

- [AVPlayerInterstitialEventRestrictionConstrainsSeekingForwardInPrimaryContent](constrainsseekingforwardinprimarycontent.md) — A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
