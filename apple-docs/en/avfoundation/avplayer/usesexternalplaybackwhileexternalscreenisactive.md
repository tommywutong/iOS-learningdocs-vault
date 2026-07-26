---
title: usesExternalPlaybackWhileExternalScreenIsActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/usesexternalplaybackwhileexternalscreenisactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/usesexternalplaybackwhileexternalscreenisactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/usesexternalplaybackwhileexternalscreenisactive.json'
content_hash: 'sha256:babe0a32665be828'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# usesExternalPlaybackWhileExternalScreenIsActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated var usesExternalPlaybackWhileExternalScreenIsActive: Bool { get set }
```

## Discussion

The player automatically switches back to the external screen mode once video playback concludes. A brief transition may be visible on the external display when automatically switching between the two modes. The default value of this property is [false](../../swift/false.md). The value of this property has no effect if [allowsExternalPlayback](allowsexternalplayback.md) is [false](../../swift/false.md).

## See Also

### Managing external playback

- [allowsExternalPlayback](allowsexternalplayback.md) — A Boolean value that indicates whether the player allows switching to external playback mode.
- [externalPlaybackActive](isexternalplaybackactive.md) — A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [externalPlaybackVideoGravity](externalplaybackvideogravity.md) — The video gravity of the player for external playback mode only.
