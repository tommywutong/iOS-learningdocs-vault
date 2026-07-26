---
title: playbackPosition
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/playbackposition
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/playbackposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-62fq2/playbackposition.json'
content_hash: 'sha256:4a176a129127d8dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-62fq2.md)

# playbackPosition

<sub>Instance Property</sub>

A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, copy, readonly) AVPlaybackUserInterfacePlaybackPosition * playbackPosition;
```
