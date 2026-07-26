---
title: playbackPosition
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/playbackposition
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/playbackposition'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacetimecontrollable-50vcy/playbackposition.json'
content_hash: 'sha256:589e74f1b164df32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceTimeControllable](../avplaybackuserinterfacetimecontrollable-50vcy.md)

# playbackPosition

<sub>Instance Property</sub>

A snapshot of the current playback position. Must be updated — with a fresh `hostTime` — on play, pause, seek, scan, and buffering state changes. Must be observable.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var playbackPosition: AVPlaybackUserInterfacePlaybackPosition { get }
```
