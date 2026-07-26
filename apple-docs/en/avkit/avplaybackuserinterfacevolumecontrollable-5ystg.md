---
title: AVPlaybackUserInterfaceVolumeControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg.json'
content_hash: 'sha256:ee2f558d8e3a1895'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlaybackUserInterfaceVolumeControllable

<sub>Protocol</sub>

Provides volume and audio muting control for media content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@protocol AVPlaybackUserInterfaceVolumeControllable <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVPlaybackUserInterfaceControllable](avplaybackuserinterfacecontrollable-7ti30.md)

## Topics

### Instance Properties

- [hasAudio](avplaybackuserinterfacevolumecontrollable-5ystg/hasaudio.md) — Indicates whether the media contains audio tracks and can produce sound output. Returns NO for video-only content, silent content, or when audio tracks are unavailable. Must be key-value observable. _(beta)_
- [muted](avplaybackuserinterfacevolumecontrollable-5ystg/muted.md) — Controls whether audio output is temporarily silenced. When YES, audio is muted regardless of the volume level setting. Must be key-value observable. _(beta)_
- [volume](avplaybackuserinterfacevolumecontrollable-5ystg/volume.md) — The audio output volume as a normalized value between 0.0 and 1.0. Must be key-value observable. _(beta)_
