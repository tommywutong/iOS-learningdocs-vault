---
title: isReady
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isready
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isready'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfaceplaybackcontrollable-9he54/isready.json'
content_hash: 'sha256:7b04792d5f307d2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfacePlaybackControllable](../avplaybackuserinterfaceplaybackcontrollable-9he54.md)

# isReady

<sub>Instance Property</sub>

Indicates whether the media source is ready to begin playback.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor var isReady: Bool { get }
```

## Discussion

This property should transition from `false` to `true` once the source has loaded enough data to start playback, and should not revert. Use [isBuffering](isbuffering.md) to track temporary stalls that may occur after this point.
