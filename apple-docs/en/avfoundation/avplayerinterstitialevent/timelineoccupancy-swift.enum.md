---
title: AVPlayerInterstitialEvent.TimelineOccupancy
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/timelineoccupancy-swift.enum.json'
content_hash: 'sha256:aaae5140fd896f96'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# AVPlayerInterstitialEvent.TimelineOccupancy

<sub>Enumeration</sub>

Constants that specify how an event occupies time on an integrated timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum TimelineOccupancy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Values

- [AVPlayerInterstitialEventTimelineOccupancySinglePoint](timelineoccupancy-swift.enum/singlepoint.md) — The event occupies a single point on the integrated timeline.
- [AVPlayerInterstitialEventTimelineOccupancyFill](timelineoccupancy-swift.enum/fill.md) — The event fills the integrated timeline with the duration of this event.

### Initializers

- [init(rawValue:)](<timelineoccupancy-swift.enum/init(rawvalue_).md>)

## See Also

### Inspecting timeline occupancy

- [timelineOccupancy](timelineoccupancy-swift.property.md) — An event’s occupancy on the integrated timeline.
- [supplementsPrimaryContent](supplementsprimarycontent.md) — A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [contentMayVary](contentmayvary.md) — A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
- [plannedDuration](plannedduration.md) — The planned duration of the event.
