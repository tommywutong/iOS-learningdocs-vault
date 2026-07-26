---
title: startDate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsegment/startdate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/startdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsegment/startdate.json'
content_hash: 'sha256:2b66effefdc2769b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSegment](../avplayeritemsegment.md)

# startDate

<sub>Instance Property</sub>

The date at which a segment starts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var startDate: Date? { get }
```

## Discussion

This value is `nil` if the primary item doesn’t contain dates.

## See Also

### Inspecting the segment

- [timeMapping](timemapping.md) — The time mapping for this segment.
- [loadedTimeRanges](loadedtimeranges-879hc.md) — The time ranges for the segment that have media data is readily available.
- [interstitialEvent](interstitialevent.md) — The associated interstitial event for this segment.
