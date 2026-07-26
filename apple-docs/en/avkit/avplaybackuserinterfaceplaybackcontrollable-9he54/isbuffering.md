---
title: isBuffering
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isbuffering.json'
content_hash: 'sha256:b3c7bea47b42484a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-9he54.md)

# isBuffering

<sub>Instance Property</sub>

Indicates whether the media source is currently stalled waiting for data.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var isBuffering: Bool { get }
```

## Discussion

Returns `true` when the source cannot immediately sustain continuous playback. This may occur both before [isReady](isready.md) becomes `true` during initial loading, and after [isReady](isready.md) is `true` during mid-playback stalls. When `true`, [isPlaying](isplaying.md) may still be `true`, indicating that playback should resume automatically once sufficient data is available.
