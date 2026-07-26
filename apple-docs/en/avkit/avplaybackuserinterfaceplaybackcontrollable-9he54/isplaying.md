---
title: isPlaying
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isplaying.json'
content_hash: 'sha256:c82aa0f17d68ad6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-9he54.md)

# isPlaying

<sub>Instance Property</sub>

Indicates whether playback is active.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var isPlaying: Bool { get set }
```

## Discussion

Setting this to `true` should start playback; setting it to `false` should pause it. This property reflects playback intent — it should remain `true` while [isBuffering](isbuffering.md) is `true`, indicating that playback should resume automatically once sufficient data is available.
