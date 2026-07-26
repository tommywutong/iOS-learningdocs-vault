---
title: buffering
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/buffering
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/buffering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/buffering.json'
content_hash: 'sha256:56b50aa6e4d062a2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-81n66.md)

# buffering

<sub>Instance Property</sub>

Indicates whether the media source is currently stalled waiting for data. Returns YES when the source cannot immediately sustain continuous playback. This may occur both before `isReady` becomes YES during initial loading, and after `isReady` is YES during mid-playback stalls. When YES, `isPlaying` may still be YES, indicating that playback should resume automatically once sufficient data is available. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly, getter=isBuffering) BOOL buffering;
```
