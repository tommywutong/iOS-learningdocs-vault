---
title: currentSegment
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentsegment
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentsegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currentsegment.json'
content_hash: 'sha256:916660c5651b8d4c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md)

# currentSegment

<sub>Instance Property</sub>

The currently playing segment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentSegment: AVPlayerItemSegment? { get }
```

## See Also

### Inspecting the snapshot

- [duration](duration.md) — The total duration of the primary item and scheduled interstitial events.
- [segments](segments.md) — The segments for this snapshot.
- [AVPlayerItemSegment](../avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentTime](currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
- [currentDate](currentdate.md) — The current date on the integrated timeline when the system created the snapshot.
