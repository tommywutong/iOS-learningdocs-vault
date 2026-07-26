---
title: 'replaceCurrentItem(with:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/replacecurrentitem(with:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/replacecurrentitem(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/replacecurrentitem%28with%3A%29.json'
content_hash: 'sha256:40fd5c9914651ea0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# replaceCurrentItem(with:)

<sub>Instance Method</sub>

Replaces the current item with a new item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func replaceCurrentItem(with item: AVPlayerItem?)
```

## Parameters

- `item` — The new item for the player object to play.

## Discussion

The player item replacement occurs immediately and the item becomes the player’s [currentItem](currentitem.md). Calling this method with the player’s current player item has no effect.

## See Also

### Managing the player item

- [currentItem](currentitem.md) — The item for which the player is currently controlling playback.
