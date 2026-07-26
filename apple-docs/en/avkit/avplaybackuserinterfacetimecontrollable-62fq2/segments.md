---
title: segments
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/segments
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/segments'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/segments.json'
content_hash: 'sha256:ba65e36431bfbebf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-62fq2.md)

# segments

<sub>Instance Property</sub>

Segments representing different content types within the timeline. All segments should be contiguous and collectively cover the entire timeline duration without gaps or overlaps. Each segment defines a specific portion of content (such as main program, advertisements, or bonus material) with its own playback characteristics. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly) NSArray<AVPlaybackUserInterfaceTimelineSegment *> * segments;
```
