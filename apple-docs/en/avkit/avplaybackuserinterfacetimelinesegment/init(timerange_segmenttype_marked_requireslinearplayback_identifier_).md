---
title: 'init(timeRange:segmentType:marked:requiresLinearPlayback:identifier:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfacetimelinesegment/init(timerange:segmenttype:marked:requireslinearplayback:identifier:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimelinesegment/init(timerange:segmenttype:marked:requireslinearplayback:identifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimelinesegment/init%28timerange%3Asegmenttype%3Amarked%3Arequireslinearplayback%3Aidentifier%3A%29.json'
content_hash: 'sha256:77a5860e53b43919'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimelineSegment](../avplaybackuserinterfacetimelinesegment.md)

# init(timeRange:segmentType:marked:requiresLinearPlayback:identifier:)

<sub>Initializer</sub>

Initializes a new timeline segment with the specified characteristics.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(timeRange: CMTimeRange, segmentType: AVPlaybackUserInterfaceTimelineSegmentType, marked: Bool, requiresLinearPlayback: Bool, identifier: String?)
```

## Parameters

- `timeRange` — The time range defining the segment’s position and duration within the timeline.

- `segmentType` — The type of content this segment represents.

- `marked` — Whether the segment should be visually highlighted in the timeline UI.

- `requiresLinearPlayback` — Whether the segment must be played sequentially without seeking or skipping.

- `identifier` — External identifier for tracking or analytics purposes.
