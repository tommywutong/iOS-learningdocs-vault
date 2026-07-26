---
title: ready
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/ready
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/ready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/ready.json'
content_hash: 'sha256:14bc266790752525'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-81n66.md)

# ready

<sub>Instance Property</sub>

Indicates whether the media source is ready to begin playback. This property should transition from NO to YES once the source has loaded enough data to start playback, and should not revert. Use `isBuffering` to track temporary stalls that may occur after this point. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly, getter=isReady) BOOL ready;
```
