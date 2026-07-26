---
title: AVInterfaceVolumeControllable
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacevolumecontrollable
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacevolumecontrollable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacevolumecontrollable.json'
content_hash: 'sha256:e484a393789ea046'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVInterfaceVolumeControllable

<sub>Protocol</sub>

Provides volume and audio muting control for media content.

<sub>tvOS, visionOS</sub>

```objc
@protocol AVInterfaceVolumeControllable <NSObject>
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [AVInterfaceControllable](avinterfacecontrollable.md)

## Topics

### Controlling volume

- [volume](avinterfacevolumecontrollable/volume.md) — The audio output level as a normalized value between 0.0 (completely silent) and 1.0 (maximum system volume). This value is independent of the muted state and represents the user’s volume preference. Must be key-value observable.
- [muted](avinterfacevolumecontrollable/muted.md) — Controls whether audio output is temporarily silenced. When YES, audio is muted regardless of the volume level setting. Must be key-value observable.
- [hasAudio](avinterfacevolumecontrollable/hasaudio.md) — Indicates whether the media contains audio tracks and can produce sound output. Returns NO for video-only content, silent content, or when audio tracks are unavailable. Must be key-value observable.
