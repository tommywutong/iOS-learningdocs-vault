---
title: AVPlayer.Status
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/status-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/status-swift.enum.json'
content_hash: 'sha256:eff012e4b26ef54d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# AVPlayer.Status

<sub>Enumeration</sub>

Status values that indicate whether a player can successfully play media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Status
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Status values

- [AVPlayerStatusUnknown](status-swift.enum/unknown.md) — A value that indicates a player hasn’t attempted to load media for playback.
- [AVPlayerStatusReadyToPlay](status-swift.enum/readytoplay.md) — A value that indicates the player is ready to media.
- [AVPlayerStatusFailed](status-swift.enum/failed.md) — A value that indicates the player can no longer play media due to an error.

### Initializers

- [init(rawValue:)](<status-swift.enum/init(rawvalue_).md>)

## See Also

### Determining player readiness

- [status](status-swift.property.md) — A value that indicates the readiness of a player object for playback.
- [error](error.md) — An error that caused a failure.
