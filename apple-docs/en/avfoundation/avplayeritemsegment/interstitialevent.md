---
title: interstitialEvent
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsegment/interstitialevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsegment/interstitialevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsegment/interstitialevent.json'
content_hash: 'sha256:151582c9ff11fca3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemSegment](../avplayeritemsegment.md)

# interstitialEvent

<sub>Instance Property</sub>

The associated interstitial event for this segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var interstitialEvent: AVPlayerInterstitialEvent? { get }
```

## Discussion

This value is `nil` for segments that represent playback of the primary item.

## See Also

### Inspecting the segment

- [timeMapping](timemapping.md) — The time mapping for this segment.
- [loadedTimeRanges](loadedtimeranges-879hc.md) — The time ranges for the segment that have media data is readily available.
- [startDate](startdate.md) — The date at which a segment starts.
