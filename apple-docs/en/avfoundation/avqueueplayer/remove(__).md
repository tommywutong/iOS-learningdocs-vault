---
title: 'remove(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avqueueplayer/remove(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer/remove%28_%3A%29.json'
content_hash: 'sha256:3239d23f8340a03d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuePlayer](../avqueueplayer.md)

# remove(_:)

<sub>Instance Method</sub>

Removes a given player item from the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func remove(_ item: AVPlayerItem)
```

## Parameters

- `item` — The player item to remove from the queue.

## Discussion

If the item is currently playing, calling this method has the same effect as calling the [- advanceToNextItem](<advancetonextitem().md>) method.

## See Also

### Managing the player queue

- [- items](<items().md>) — Returns an array of the currently enqueued items.
- [- advanceToNextItem](<advancetonextitem().md>) — Ends playback of the current item and starts playback of the next item in the player’s queue.
- [- canInsertItem:afterItem:](<caninsert(__after_).md>) — Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [- insertItem:afterItem:](<insert(__after_).md>) — Inserts a player item after another player item in the queue.
- [- removeAllItems](<removeallitems().md>) — Removes all player items from the queue.
