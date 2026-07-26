---
title: AVPlayer.Status.failed
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/status-swift.enum/failed
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.enum/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/status-swift.enum/failed.json'
content_hash: 'sha256:0880c3319c0377a1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVPlayer](../../avplayer.md) · [Status](../status-swift.enum.md)

# AVPlayer.Status.failed

<sub>Case</sub>

A value that indicates the player can no longer play media due to an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed
```

## Discussion

Inspect the value of the player’s [error](../error.md) property to determine the details of the failure.

## See Also

### Status values

- [AVPlayerStatusUnknown](unknown.md) — A value that indicates a player hasn’t attempted to load media for playback.
- [AVPlayerStatusReadyToPlay](readytoplay.md) — A value that indicates the player is ready to media.
