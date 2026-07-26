---
title: requiresLinearPlayback
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacetimelinesegment/requireslinearplayback
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/requireslinearplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacetimelinesegment/requireslinearplayback.json'
content_hash: 'sha256:d45107031df5ca4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceTimelineSegment](../avinterfacetimelinesegment.md)

# requiresLinearPlayback

<sub>Instance Property</sub>

Indicates whether this segment must be played sequentially without seeking or skipping. Typically used for advertisements or important announcements.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) BOOL requiresLinearPlayback;
```

## See Also

### Inspecting the segment

- [timeRange](timerange.md) — The time range defining the segment’s position and duration within the overall timeline.
- [identifier](identifier.md) — Optional external identifier for tracking or analytics purposes. May correspond to advertisement IDs, chapter markers, or other external systems.
