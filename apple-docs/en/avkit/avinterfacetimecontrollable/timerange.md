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
doc_path: /documentation/avkit/avinterfacetimecontrollable/timerange
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacetimecontrollable/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacetimecontrollable/timerange.json'
content_hash: 'sha256:a198cb67fee569ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceTimeControllable](../avinterfacetimecontrollable.md)

# timeRange

<sub>Instance Property</sub>

The time range representing the total duration and bounds of the media content. This defines the overall playable timeline, with all segments and seekable ranges falling within this range. Must be key-value observable.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) CMTimeRange timeRange;
```

## See Also

### Inspecting the timeline

- [currentPlaybackPosition](currentplaybackposition.md) — The current playback position within the media time, expressed in seconds from the start of the content. This value should be within the bounds defined by the start and duration properties and represents the exact temporal position of playback. Must be key-value observable.
- [currentSegment](currentsegment.md) — The segment containing the current playback position. This property automatically updates as playback progresses through different timeline segments. Use this to determine the current content type (primary vs. secondary) and any special playback characteristics that apply to the current position. Must be key-value observable.
- [seekableTimeRanges](seekabletimeranges.md) — An array of time ranges within the timeline where seeking operations are permitted. Each range is represented as an NSValue wrapping a CMTimeRange structure, defining portions of the timeline where users can jump to specific time positions during playback. If nil, the entire content defined by timeRange is considered seekable. When provided, each range must be a subset of the overall timeRange and should not overlap with other seekable ranges. An empty array means the entire content defined by timeRange is not seekable. Seekable ranges typically exclude segments where requiresLinearPlayback is YES, such as advertisements, mandatory content, or licensing-restricted portions. The array should contain ranges in chronological order for optimal performance. Must be key-value observable.
- [segments](segments.md) — Segments representing different content types within the timeline. All segments should be contiguous and collectively cover the entire timeline duration without gaps or overlaps. Each segment defines a specific portion of content (such as main program, advertisements, or bonus material) with its own playback characteristics. Must be key-value observable.
