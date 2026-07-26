---
title: alignsResumptionWithPrimarySegmentBoundary
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/alignsresumptionwithprimarysegmentboundary.json'
content_hash: 'sha256:0cdf188c80f14ee3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# alignsResumptionWithPrimarySegmentBoundary

<sub>Instance Property</sub>

A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var alignsResumptionWithPrimarySegmentBoundary: Bool { get set }
```

## Discussion

If the value is [true](../../swift/true.md), the system adjusts the resumption time of primary playback following an interstitial to the nearest segment boundary when the primary player is playing an HTTP Live Streaming asset.

## See Also

### Inspecting timing

- [time](time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [date](date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [willPlayOnce](willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [resumptionOffset](resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [playoutLimit](playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
