---
title: 'initWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avinterfacetimelinesegment/initwithtimerange:auxiliarycontent:marked:requireslinearplayback:identifier:'
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacetimelinesegment/initwithtimerange:auxiliarycontent:marked:requireslinearplayback:identifier:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacetimelinesegment/initwithtimerange%3Aauxiliarycontent%3Amarked%3Arequireslinearplayback%3Aidentifier%3A.json'
content_hash: 'sha256:babc3603df777fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceTimelineSegment](../avinterfacetimelinesegment.md)

# initWithTimeRange:auxiliaryContent:marked:requiresLinearPlayback:identifier:

<sub>Instance Method</sub>

Initializes a new timeline segment with the specified characteristics.

<sub>tvOS, visionOS</sub>

```objc
- (instancetype) initWithTimeRange:(CMTimeRange) timeRange auxiliaryContent:(BOOL) auxiliaryContent marked:(BOOL) marked requiresLinearPlayback:(BOOL) requiresLinearPlayback identifier:(NSString *) identifier;
```

## Parameters

- `timeRange` — The time range defining the segment’s position and duration within the timeline.

- `auxiliaryContent` — Whether the segment contains main or auxiliary content.

- `marked` — Whether the segment should be visually highlighted in the timeline UI.

- `requiresLinearPlayback` — Whether the segment must be played sequentially without seeking or skipping.

- `identifier` — External identifier for tracking or analytics purposes.
