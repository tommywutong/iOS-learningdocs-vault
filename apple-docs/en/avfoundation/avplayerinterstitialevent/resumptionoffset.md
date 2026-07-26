---
title: resumptionOffset
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/resumptionoffset
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/resumptionoffset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/resumptionoffset.json'
content_hash: 'sha256:c25b9614ae7e1d29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# resumptionOffset

<sub>Instance Property</sub>

A time offset at which playback of primary content resumes after interstitial content finishes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var resumptionOffset: CMTime { get set }
```

## Discussion

This property supports definite time values. Specify [indefinite](../../coremedia/cmtime/indefinite.md) to indicate that the effective resumption time offset should align with the clock time elapsed during interstitial playback; this value is typically suitable for live broadcasts.

The default value is [zero](../../coremedia/cmtime/zero.md).

## See Also

### Inspecting timing

- [time](time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [date](date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [willPlayOnce](willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [playoutLimit](playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
