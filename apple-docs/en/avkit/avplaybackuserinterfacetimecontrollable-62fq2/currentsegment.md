---
title: currentSegment
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/currentsegment
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/currentsegment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/currentsegment.json'
content_hash: 'sha256:46c0c4d03191ca61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-62fq2.md)

# currentSegment

<sub>Instance Property</sub>

The segment containing the current playback position. This property automatically updates as playback progresses through different timeline segments. Use this to determine the current content type (primary vs. secondary) and any special playback characteristics that apply to the current position. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly) AVPlaybackUserInterfaceTimelineSegment * currentSegment;
```
