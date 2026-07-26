---
title: AVPlaybackUserInterfaceVolumeControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [swift, swift, swift]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacevolumecontrollable-4vgi1
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacevolumecontrollable-4vgi1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacevolumecontrollable-4vgi1.json'
content_hash: 'sha256:baa5da29c365293d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceVolumeControllable

<sub>Protocol</sub>

Provides volume and audio muting control for media content.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
@MainActor protocol AVPlaybackUserInterfaceVolumeControllable : AnyObject, Observable
```

## Relationships

- **Inherits From**: [Observable](../observation/observable.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-92fri.md)

## Topics

### Instance Properties

- [hasAudio](avplaybackuserinterfacevolumecontrollable-4vgi1/hasaudio.md) — Indicates whether the media contains audio tracks. _(beta)_
- [isMuted](avplaybackuserinterfacevolumecontrollable-4vgi1/ismuted.md) — Controls whether audio output is temporarily silenced. _(beta)_
- [volume](avplaybackuserinterfacevolumecontrollable-4vgi1/volume.md) — The audio output volume as a normalized value between 0.0 and 1.0. _(beta)_
