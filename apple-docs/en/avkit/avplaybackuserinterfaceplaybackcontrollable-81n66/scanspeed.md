---
title: scanSpeed
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-81n66/scanspeed.json'
content_hash: 'sha256:20fe600280395170'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-81n66.md)

# scanSpeed

<sub>Instance Property</sub>

The speed multiplier used during scanning (fast-forward or rewind). This is a transient override that is active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, readwrite) float scanSpeed;
```
