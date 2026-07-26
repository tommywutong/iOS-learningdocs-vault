---
title: disconnectedFromSystemAudio
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayer/disconnectedfromsystemaudio
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/disconnectedfromsystemaudio'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/disconnectedfromsystemaudio.json'
content_hash: 'sha256:bfb00dffaff73f72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# disconnectedFromSystemAudio

<sub>Instance Property</sub>

Indicates whether the player is disconnected from system audio.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var disconnectedFromSystemAudio: Bool { get }
```

## Discussion

When NO (the default), the player is connected to system audio and coordinates with the application’s shared `AVAudioSession`. This implies that the player will activate the audio session when playback starts, render audio, and automatically reconfigure itself after events like route changes.

When YES, the player is disconnected from system audio and will not interact with the audio session. It will not activate the audio session when starting and it does not reconfigure after route changes. Specifically, this implies that such a player will not play audio until the property changes back to NO.

The value of this property can be changed dynamically during playback using setDisconnectedFromSystemAudio:completionHandler:.
