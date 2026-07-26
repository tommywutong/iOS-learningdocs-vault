---
title: 'canInsert(_:after:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avqueueplayer/caninsert(_:after:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer/caninsert(_:after:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer/caninsert%28_%3Aafter%3A%29.json'
content_hash: 'sha256:57c4150cb241f133'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuePlayer](../avqueueplayer.md)

# canInsert(_:after:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func canInsert(_ item: AVPlayerItem, after afterItem: AVPlayerItem?) -> Bool
```

## Parameters

- `item` — The player item to insert.

- `afterItem` — The player item in the queue to follow. Pass `nil` to test if you can append the item to the queue.

## Return Value

[true](../../swift/true.md) if `item` can be appended to the queue, otherwise [false](../../swift/false.md).

## Discussion

Adding the same item to a player at more than one position in the queue isn’t supported.

## See Also

### Managing the player queue

- [- items](<items().md>) — Returns an array of the currently enqueued items.
- [- advanceToNextItem](<advancetonextitem().md>) — Ends playback of the current item and starts playback of the next item in the player’s queue.
- [- insertItem:afterItem:](<insert(__after_).md>) — Inserts a player item after another player item in the queue.
- [- removeItem:](<remove(__).md>) — Removes a given player item from the queue.
- [- removeAllItems](<removeallitems().md>) — Removes all player items from the queue.
