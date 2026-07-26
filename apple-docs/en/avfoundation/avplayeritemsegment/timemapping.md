---
title: timeMapping
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsegment/timemapping
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/timemapping'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsegment/timemapping.json'
content_hash: 'sha256:cba2b1c07043c7b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSegment](../avplayeritemsegment.md)

# timeMapping

<sub>Instance Property</sub>

The time mapping for this segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timeMapping: CMTimeMapping { get }
```

## Discussion

The time mapping’s source time range represents the start time and duration in the segment source’s timeline, either the primary item or interstitial event. The target time range represents the start time and duration in the integrated timeline. For interstitial events that occupy a single point, the target’s duration is [zero](../../coremedia/cmtime/zero.md).

## See Also

### Inspecting the segment

- [loadedTimeRanges](loadedtimeranges-879hc.md) — The time ranges for the segment that have media data is readily available.
- [startDate](startdate.md) — The date at which a segment starts.
- [interstitialEvent](interstitialevent.md) — The associated interstitial event for this segment.
