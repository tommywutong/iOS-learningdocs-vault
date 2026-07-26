---
title: externalPlaybackVideoGravity
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS 9.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/externalplaybackvideogravity
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/externalplaybackvideogravity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/externalplaybackvideogravity.json'
content_hash: 'sha256:6a0641f850765fe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# externalPlaybackVideoGravity

<sub>Instance Property</sub>

The video gravity of the player for external playback mode only.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated var externalPlaybackVideoGravity: AVLayerVideoGravity { get set }
```

## Discussion

Valid values are [AVLayerVideoGravityResize](../avlayervideogravity/resize.md), [AVLayerVideoGravityResizeAspectFill](../avlayervideogravity/resizeaspectfill.md), or [AVLayerVideoGravityResizeAspect](../avlayervideogravity/resizeaspect.md).

## See Also

### Managing external playback

- [allowsExternalPlayback](allowsexternalplayback.md) — A Boolean value that indicates whether the player allows switching to external playback mode.
- [externalPlaybackActive](isexternalplaybackactive.md) — A Boolean value that indicates whether the player is currently playing video in external playback mode.
- [usesExternalPlaybackWhileExternalScreenIsActive](usesexternalplaybackwhileexternalscreenisactive.md) — A Boolean value that indicates whether the player should automatically switch to external playback mode while the external screen mode is active.
