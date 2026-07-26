---
title: playoutLimit
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/playoutlimit
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/playoutlimit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/playoutlimit.json'
content_hash: 'sha256:98b81527f5d64940'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# playoutLimit

<sub>Instance Property</sub>

The time offset at which playback of the interstitial ends.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var playoutLimit: CMTime { get set }
```

## Discussion

This value can be any positive numeric value, or [invalid](../../coremedia/cmtime/invalid.md) (the default) which indicates no limit.

## See Also

### Inspecting timing

- [time](time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [date](date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [willPlayOnce](willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [resumptionOffset](resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
