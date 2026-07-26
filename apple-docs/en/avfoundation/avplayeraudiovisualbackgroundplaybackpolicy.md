---
title: AVPlayerAudiovisualBackgroundPlaybackPolicy
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeraudiovisualbackgroundplaybackpolicy
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeraudiovisualbackgroundplaybackpolicy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeraudiovisualbackgroundplaybackpolicy.json'
content_hash: 'sha256:22c1b6b2a15ec004'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerAudiovisualBackgroundPlaybackPolicy

<sub>Enumeration</sub>

Policies that describe playback behavior when an app transitions to the background while playing video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVPlayerAudiovisualBackgroundPlaybackPolicy
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Policies

- [AVPlayerAudiovisualBackgroundPlaybackPolicyAutomatic](avplayeraudiovisualbackgroundplaybackpolicy/automatic.md) — The system decides whether playback continues.
- [AVPlayerAudiovisualBackgroundPlaybackPolicyContinuesIfPossible](avplayeraudiovisualbackgroundplaybackpolicy/continuesifpossible.md) — The app continues playback, if possible.
- [AVPlayerAudiovisualBackgroundPlaybackPolicyPauses](avplayeraudiovisualbackgroundplaybackpolicy/pauses.md) — The app pauses playback.

### Initializers

- [init(rawValue:)](<avplayeraudiovisualbackgroundplaybackpolicy/init(rawvalue_).md>)

## See Also

### Configuring background playback

- [audiovisualBackgroundPlaybackPolicy](avplayer/audiovisualbackgroundplaybackpolicy.md) — A policy that determines how playback of audiovisual media continues when the app transitions to the background.
