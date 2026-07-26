---
title: removeAllItems()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avqueueplayer/removeallitems()
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer/removeallitems()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer/removeallitems%28%29.json'
content_hash: 'sha256:ff442910067279ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuePlayer](../avqueueplayer.md)

# removeAllItems()

<sub>Instance Method</sub>

Removes all player items from the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func removeAllItems()
```

## Discussion

Calling this method removes all currently enqueued player items and stops playback.

## See Also

### Managing the player queue

- [- items](<items().md>) — Returns an array of the currently enqueued items.
- [- advanceToNextItem](<advancetonextitem().md>) — Ends playback of the current item and starts playback of the next item in the player’s queue.
- [- canInsertItem:afterItem:](<caninsert(__after_).md>) — Returns a Boolean value that indicates whether you can insert a player item into the player’s queue.
- [- insertItem:afterItem:](<insert(__after_).md>) — Inserts a player item after another player item in the queue.
- [- removeItem:](<remove(__).md>) — Removes a given player item from the queue.
