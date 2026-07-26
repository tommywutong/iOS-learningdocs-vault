---
title: timelineOccupancy
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.property.json'
content_hash: 'sha256:f286d84a60a48b50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# timelineOccupancy

<sub>Instance Property</sub>

An event’s occupancy on the integrated timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var timelineOccupancy: AVPlayerInterstitialEvent.TimelineOccupancy { get set }
```

## Discussion

The default value is [AVPlayerInterstitialEventTimelineOccupancySinglePoint](timelineoccupancy-swift.enum/singlepoint.md).

## See Also

### Inspecting timeline occupancy

- [TimelineOccupancy](timelineoccupancy-swift.enum.md) — Constants that specify how an event occupies time on an integrated timeline.
- [supplementsPrimaryContent](supplementsprimarycontent.md) — A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [contentMayVary](contentmayvary.md) — A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [plannedDuration](plannedduration.md) — The planned duration of the event.
