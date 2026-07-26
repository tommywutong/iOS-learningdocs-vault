---
title: plannedDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/plannedduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/plannedduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/plannedduration.json'
content_hash: 'sha256:c4960ce48909eb63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# plannedDuration

<sub>Instance Property</sub>

The planned duration of the event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var plannedDuration: CMTime { get set }
```

## Discussion

The default value is [zero](../../coremedia/cmtime/zero.md).

## See Also

### Inspecting timeline occupancy

- [timelineOccupancy](timelineoccupancy-swift.property.md) — An event’s occupancy on the integrated timeline.
- [TimelineOccupancy](timelineoccupancy-swift.enum.md) — Constants that specify how an event occupies time on an integrated timeline.
- [supplementsPrimaryContent](supplementsprimarycontent.md) — A Boolean value that indicates whether an event supplements the primary content and should present with the primary item.
- [contentMayVary](contentmayvary.md) — A Boolean value that indicates whether an event’s content is dynamic and the server may respond with different interstitial assets for other participants in a coordinated playback session.
