---
title: contentMayVary
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/contentmayvary
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/contentmayvary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/contentmayvary.json'
content_hash: 'sha256:d1b755bfb48f2853'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# contentMayVary

<sub>Instance Property</sub>

A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var contentMayVary: Bool { get set }
```

## Discussion

If the value is [false](../../swift/false.md), the primary asset participates in coordinated playback, this event does as well.

The default value is [true](../../swift/true.md).

## See Also

### Inspecting timeline occupancy

- [timelineOccupancy](timelineoccupancy-swift.property.md) — An event’s occupancy on the integrated timeline.
- [TimelineOccupancy](timelineoccupancy-swift.enum.md) — Constants that specify how an event occupies time on an integrated timeline.
- [supplementsPrimaryContent](supplementsprimarycontent.md) — A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [plannedDuration](plannedduration.md) — The planned duration of the event.
