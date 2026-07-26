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
doc_path: /documentation/avfoundation/avplayeritem/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/status-swift.property.json'
content_hash: 'sha256:bba2b44c6c938321'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# status

<sub>Instance Property</sub>

The status of the player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var status: AVPlayerItem.Status { get }
```

## Discussion

When a player item is created, its [status](status-swift.property.md) is [AVPlayerItemStatusUnknown](status-swift.enum/unknown.md), meaning its media hasn’t been loaded and has not yet been enqueued for playback. Associating a player item with an [AVPlayer](../avplayer.md) immediately begins enqueuing the item’s media and preparing it for playback. When the player item’s media has been loaded and is ready for use, its status will change to [AVPlayerItemStatusReadyToPlay](status-swift.enum/readytoplay.md). You can observe this change using key-value observing.

For possible values, see [Status](status-swift.enum.md).

## See Also

### Determining readiness

- [Status](status-swift.enum.md) — The statuses for a player item.
- [error](error.md) — The error that caused the player item to fail.
