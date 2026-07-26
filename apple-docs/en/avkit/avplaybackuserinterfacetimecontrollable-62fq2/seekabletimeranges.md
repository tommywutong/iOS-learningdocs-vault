---
title: seekableTimeRanges
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/seekabletimeranges.json'
content_hash: 'sha256:f4a6091d38b95490'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-62fq2.md)

# seekableTimeRanges

<sub>Instance Property</sub>

An array of time ranges within the timeline where seeking operations are permitted. Each range is represented as an NSValue wrapping a CMTimeRange structure, defining portions of the timeline where users can jump to specific time positions during playback. If `nil`, the entire content defined by timeRange is considered seekable. When provided, each range must be a subset of the overall timeRange and should not overlap with other seekable ranges. An empty array means the entire content defined by timeRange is not seekable. Seekable ranges typically exclude segments where requiresLinearPlayback is YES, such as advertisements, mandatory content, or licensing-restricted portions. The array should contain ranges in chronological order for optimal performance. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSValue *> * seekableTimeRanges;
```
