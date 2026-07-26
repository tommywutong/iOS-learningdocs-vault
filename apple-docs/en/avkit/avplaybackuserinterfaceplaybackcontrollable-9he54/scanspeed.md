---
title: scanSpeed
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/scanspeed
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/scanspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/scanspeed.json'
content_hash: 'sha256:a8b49bb353cdf5b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-9he54.md)

# scanSpeed

<sub>Instance Property</sub>

The speed multiplier used during scanning (fast-forward or rewind). This is a transient override active only while `state` is scanning. It does not affect `playbackSpeed`. When scanning ends, playback resumes at `playbackSpeed`.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var scanSpeed: Float { get set }
```
