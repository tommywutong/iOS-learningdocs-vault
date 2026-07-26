---
title: loadedTimeRanges
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsegment/loadedtimeranges-879hc
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/loadedtimeranges-879hc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsegment/loadedtimeranges-879hc.json'
content_hash: 'sha256:a69e51d77bf5abaf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSegment](../avplayeritemsegment.md)

# loadedTimeRanges

<sub>Instance Property</sub>

The time ranges for the segment that have media data is readily available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@nonobjc var loadedTimeRanges: [CMTimeRange] { get }
```

## Discussion

The loaded time ranges might be discontinuous.

## See Also

### Inspecting the segment

- [timeMapping](timemapping.md) — The time mapping for this segment.
- [startDate](startdate.md) — The date at which a segment starts.
- [interstitialEvent](interstitialevent.md) — The associated interstitial event for this segment.
