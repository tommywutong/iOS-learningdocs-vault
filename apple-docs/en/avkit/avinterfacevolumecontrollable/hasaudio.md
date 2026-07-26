---
title: hasAudio
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avinterfacevolumecontrollable/hasaudio
source_url: 'https://developer.apple.com/documentation/avkit/avinterfacevolumecontrollable/hasaudio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avinterfacevolumecontrollable/hasaudio.json'
content_hash: 'sha256:c592f6240169e941'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVInterfaceVolumeControllable](../avinterfacevolumecontrollable.md)

# hasAudio

<sub>Instance Property</sub>

Indicates whether the media contains audio tracks and can produce sound output. Returns NO for video-only content, silent content, or when audio tracks are unavailable. Must be key-value observable.

<sub>tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) BOOL hasAudio;
```

## See Also

### Controlling volume

- [volume](volume.md) — The audio output level as a normalized value between 0.0 (completely silent) and 1.0 (maximum system volume). This value is independent of the muted state and represents the user’s volume preference. Must be key-value observable.
- [muted](muted.md) — Controls whether audio output is temporarily silenced. When YES, audio is muted regardless of the volume level setting. Must be key-value observable.
