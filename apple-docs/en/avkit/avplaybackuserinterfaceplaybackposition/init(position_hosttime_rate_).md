---
title: 'init(position:hostTime:rate:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift, occ, occ, occ]
beta: true
deprecated: false
doc_path: '/documentation/avkit/avplaybackuserinterfaceplaybackposition/init(position:hosttime:rate:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackposition/init(position:hosttime:rate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackposition/init%28position%3Ahosttime%3Arate%3A%29.json'
content_hash: 'sha256:6c9b698aa4f8b60d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackPosition](../avplaybackuserinterfaceplaybackposition.md)

# init(position:hostTime:rate:)

<sub>Initializer</sub>

Creates a new playback position snapshot.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(position: CMTime, hostTime: CMTime, rate: Float)
```

## Parameters

- `position` — The playback position at `hostTime`.

- `hostTime` — The mach host time at which `position` was accurate.

- `rate` — The rate of position advancement at the time of the snapshot.

## Return Value

A new playback position snapshot.
