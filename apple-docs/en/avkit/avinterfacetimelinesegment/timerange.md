---
title: timeRange
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacetimelinesegment/timerange
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacetimelinesegment/timerange.json'
content_hash: 'sha256:467672d1913c5d42'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceTimelineSegment](../avinterfacetimelinesegment.md)

# timeRange

<sub>Instance Property</sub>

The time range defining the segment’s position and duration within the overall timeline.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```

## See Also

### Inspecting the segment

- [identifier](identifier.md) — Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
- [requiresLinearPlayback](requireslinearplayback.md) — Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.
