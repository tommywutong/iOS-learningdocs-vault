---
title: 'insert(_:after:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avqueueplayer/insert(_:after:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer/insert(_:after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer/insert%28_%3Aafter%3A%29.json'
content_hash: 'sha256:31c597ba22e2569e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuePlayer](../avqueueplayer.md)

# insert(_:after:)

<sub>Instance Method</sub>

Inserts a player item after another player item in the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func insert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?)
```

## Parameters

- `item` — The item to insert into the queue.

- `afterItem` — The player item in the queue to follow. Pass `nil` to append the item to the queue.

## See Also

### Managing the player queue

- [- items](<items().md>) — Returns an array of the currently enqueued items.
- [- advanceToNextItem](<advancetonextitem().md>) — Ends playback of the current item and starts playback of the next item in the player’s queue.
- [- canInsertItem:afterItem:](<caninsert(__after_).md>) — Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [- removeItem:](<remove(__).md>) — Removes a given player item from the queue.
- [- removeAllItems](<removeallitems().md>) — Removes all player items from the queue.
