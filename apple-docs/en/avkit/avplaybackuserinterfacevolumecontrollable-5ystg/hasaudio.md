---
title: hasAudio
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta]
languages: [occ, occ, occ]
beta: true
deprecated: false
doc_path: /documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg/hasaudio
source_url: 'https://developer.apple.com/documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg/hasaudio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplaybackuserinterfacevolumecontrollable-5ystg/hasaudio.json'
content_hash: 'sha256:bf103fdcc02cdbf5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlaybackUserInterfaceVolumeControllable](../avplaybackuserinterfacevolumecontrollable-5ystg.md)

# hasAudio

<sub>Instance Property</sub>

Indicates whether the media contains audio tracks and can produce sound output. Returns NO for video-only content, silent content, or when audio tracks are unavailable. Must be key-value observable.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```objc
@property (nonatomic, readonly) BOOL hasAudio;
```
