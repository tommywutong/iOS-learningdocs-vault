---
title: 'init(player:templateItem:timeRange:existingItemsOrdering:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerlooper/init(player:templateitem:timerange:existingitemsordering:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/init(player:templateitem:timerange:existingitemsordering:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/init%28player%3Atemplateitem%3Atimerange%3Aexistingitemsordering%3A%29.json'
content_hash: 'sha256:d62480c9da793c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# init(player:templateItem:timeRange:existingItemsOrdering:)

<sub>Initializer</sub>

Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(player: AVQueuePlayer, templateItem itemToLoop: AVPlayerItem, timeRange loopRange: CMTimeRange, existingItemsOrdering itemOrdering: AVPlayerLooper.ItemOrdering)
```

## Parameters

- `player` — A queue player to control playback.

- `itemToLoop` — A player item to loop.

- `loopRange` — The player item time range to loop. Passing a value of [invalid](../../coremedia/cmtimerange/invalid.md) is equivalent to a time range of [0, player item’s duration].

- `itemOrdering` — A value that indicates whether the looper inserts replica items before or after existing items in the specified queue player.

## Discussion

The player looper doesn’t use the player item you specify for playback, and instead uses it as a template to create at least three player item replicas that it uses for looping playback. Because the looper only uses the player item as a template, any changes that you make to it after initialization aren’t reflected in the looping playback.

> [!important] Important
> Load the [duration](../avpartialasyncproperty/duration.md) value of a player item’s asset before passing the item to the looper to prevent blocking the calling thread until the duration is known.

## Topics

### Item ordering

- [ItemOrdering](itemordering.md) — Constants that define the ordering of items in a player looper.

## See Also

### Creating a player looper

- [+ playerLooperWithPlayer:templateItem:](<init(player_templateitem_).md>) — Creates a player looper that continuously plays the full duration of a player item.
- [- initWithPlayer:templateItem:timeRange:](<init(player_templateitem_timerange_).md>) — Creates a player looper that continuously plays the specified time range of a player item.
