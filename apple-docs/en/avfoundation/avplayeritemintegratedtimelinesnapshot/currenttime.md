---
title: currentTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currenttime
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currenttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemintegratedtimelinesnapshot/currenttime.json'
content_hash: 'sha256:65a2d1387180429c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItemIntegratedTimelineSnapshot](../avplayeritemintegratedtimelinesnapshot.md)

# currentTime

<sub>Instance Property</sub>

The current time on the integrated timeline when the system created the snapshot.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var currentTime: CMTime { get }
```

## Discussion

This value doesn’t change as time progresses.

## See Also

### Inspecting the snapshot

- [duration](duration.md) — The total duration of the primary item and scheduled interstitial events.
- [currentSegment](currentsegment.md) — The currently playing segment.
- [segments](segments.md) — The segments for this snapshot.
- [AVPlayerItemSegment](../avplayeritemsegment.md) — An immutable object that represents a segment of time on the integrated timeline.
- [currentDate](currentdate.md) — The current date on the integrated timeline when the system created the snapshot.
