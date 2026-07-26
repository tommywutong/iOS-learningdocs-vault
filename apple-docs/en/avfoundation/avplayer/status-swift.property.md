---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/status-swift.property.json'
content_hash: 'sha256:76ab735f41f0b579'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# status

<sub>Instance Property</sub>

A value that indicates the readiness of a player object for playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var status: AVPlayer.Status { get }
```

## Discussion

If the value of this property is [AVPlayerStatusFailed](status-swift.enum/failed.md), check the value of the player’s [error](error.md) property to determine the nature of the failure. If a player reaches a failed state, you can’t use it for playback, and instead need to create a new instance.

This property is key-value observable.

> [!note] Note
> The player’s [status](status-swift.property.md) doesn’t indicate its readiness to play a specific player item. You should instead use the [status](../avplayeritem/status-swift.property.md) property of [AVPlayerItem](../avplayeritem.md) to make that determination.

## See Also

### Determining player readiness

- [Status](status-swift.enum.md) — Status values that indicate whether a player can successfully play media.
- [error](error.md) — An error that caused a failure.
