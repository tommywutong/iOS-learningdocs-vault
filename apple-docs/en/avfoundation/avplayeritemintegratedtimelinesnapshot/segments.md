---
title: segments
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/segments
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/segments.json'
content_hash: 'sha256:fbadb960ab3509b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md)

# segments

<sub>Instance Property</sub>

The segments for this snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var segments: [AVPlayerItemSegment] { get }
```

## Discussion

The system presents segments in chronological order, contiguous from the previous element, and non-overlapping.

## See Also

### Inspecting the snapshot

- [duration](duration.md) — The total duration of the primary item and scheduled interstitial events.
- [currentSegment](currentsegment.md) — The currently playing segment.
- [AVPlayerItemSegment](../avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentTime](currenttime.md) — The current time on the integrated timeline when the system created the snapshot.
- [currentDate](currentdate.md) — The current date on the integrated timeline when the system created the snapshot.
