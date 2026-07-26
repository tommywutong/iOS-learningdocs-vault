---
title: date
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/date
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/date'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/date.json'
content_hash: 'sha256:0057868d1df4cff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# date

<sub>Instance Property</sub>

A date within the date range of the primary content that playback of interstitial content begins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var date: Date? { get set }
```

## Discussion

This property value is `nil` if you initialized the event with a time instead of a date.

## See Also

### Inspecting timing

- [time](time.md) — A time within the timeline of the primary content that playback of interstitial content begins.
- [willPlayOnce](willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [resumptionOffset](resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [playoutLimit](playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
