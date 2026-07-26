---
title: AVPlayerInterstitialEventRestrictionDefaultPolicy
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Enumeration Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictiondefaultpolicy
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictiondefaultpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventrestrictions/avplayerinterstitialeventrestrictiondefaultpolicy.json'
content_hash: 'sha256:af5f92a0b0c532bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [Restrictions](../avplayerinterstitialevent/restrictions-swift.struct.md)

# AVPlayerInterstitialEventRestrictionDefaultPolicy

<sub>Enumeration Case</sub>

The default restriction policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
AVPlayerInterstitialEventRestrictionDefaultPolicy
```

## Discussion

By default, an event imposes no restrictions.

## See Also

### Configure

- [AVPlayerInterstitialEventRestrictionConstrainsSeekingForwardInPrimaryContent](../avplayerinterstitialevent/restrictions-swift.struct/constrainsseekingforwardinprimarycontent.md) — A restriction that indicates the event doesn’t allow seeking forward within an interstitial item.
- [AVPlayerInterstitialEventRestrictionRequiresPlaybackAtPreferredRateForAdvancement](../avplayerinterstitialevent/restrictions-swift.struct/requiresplaybackatpreferredrateforadvancement.md) — A restriction that indicates the event doesn’t allow advancing the current time within an interstitial item.
- [AVPlayerInterstitialEventRestrictionNone](avplayerinterstitialeventrestrictionnone.md) — A value that indicates no restrictions on playback of primary or interstitial content.
