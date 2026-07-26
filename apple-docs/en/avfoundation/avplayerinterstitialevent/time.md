---
title: time
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/time
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/time'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/time.json'
content_hash: 'sha256:2837f55101690ec0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# time

<sub>Instance Property</sub>

A time within the timeline of the primary content that playback of interstitial content begins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var time: CMTime { get set }
```

## Discussion

This property value is [invalid](../../coremedia/cmtime/invalid.md) if you initialized the event with a date instead of a time.

## See Also

### Inspecting timing

- [date](date.md) — A date within the date range of the primary content that playback of interstitial content begins.
- [willPlayOnce](willplayonce.md) — A Boolean value that indicates whether to schedule this event one time only and suppress subsequent replay.
- [resumptionOffset](resumptionoffset.md) — A time offset at which playback of primary content resumes after interstitial content finishes.
- [playoutLimit](playoutlimit.md) — The time offset at which playback of the interstitial ends.
- [alignsStartWithPrimarySegmentBoundary](alignsstartwithprimarysegmentboundary.md) — A Boolean value that indicates whether the start time of interstitial playback should snap to a segment boundary of the primary asset.
- [alignsResumptionWithPrimarySegmentBoundary](alignsresumptionwithprimarysegmentboundary.md) — A Boolean value that indicates whether the resumption time of primary playback should snap to a segment boundary of the primary asset.
