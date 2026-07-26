---
title: allowsExternalPlayback
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/allowsexternalplayback
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/allowsexternalplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/allowsexternalplayback.json'
content_hash: 'sha256:42ebf41cbf3a4565'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# allowsExternalPlayback

<sub>Instance Property</sub>

A Boolean value that indicates whether the player allows switching to external playback mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
nonisolated var allowsExternalPlayback: Bool { get set }
```

## Discussion

The default value of this property is [true](../../swift/true.md).

## See Also

### Managing external playback

- [externalPlaybackActive](isexternalplaybackactive.md) — A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [usesExternalPlaybackWhileExternalScreenIsActive](usesexternalplaybackwhileexternalscreenisactive.md) — A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.
- [externalPlaybackVideoGravity](externalplaybackvideogravity.md) — The video gravity of the player for external playback mode only.
