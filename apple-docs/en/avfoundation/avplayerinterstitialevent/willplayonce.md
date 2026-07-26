---
title: willPlayOnce
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/willplayonce
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/willplayonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/willplayonce.json'
content_hash: 'sha256:0cd1cc169661af7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# willPlayOnce

<sub>Instance Property</sub>

A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var willPlayOnce: Bool { get set }
```

## Discussion

The “once” provision takes effect at the start of interstitial playback. The system doesn’t schedule playback again even if the first playback is canceled before completion.

## See Also

### Inspecting timing

- [time](time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [date](date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [resumptionOffset](resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [playoutLimit](playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
