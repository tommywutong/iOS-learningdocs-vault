---
title: 'init(player:templateItem:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerlooper/init(player:templateitem:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/init(player:templateitem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/init%28player%3Atemplateitem%3A%29.json'
content_hash: 'sha256:3b9b8463a5a9a066'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# init(player:templateItem:)

<sub>Initializer</sub>

Creates a player looper that continuously plays the full duration of a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init(player: AVQueuePlayer, templateItem itemToLoop: AVPlayerItem)
```

## Parameters

- `player` — The queue player to use for playback. The player must not be `nil`.

- `itemToLoop` — The player item to loop, which must not be `nil`.

## Return Value

An new instance of `AVPlayerLooper`.

## Discussion

Creating an instance of this class using this method is equivalent to calling [- initWithPlayer:templateItem:timeRange:](<init(player_templateitem_timerange_).md>) and passing a value of [invalid](../../coremedia/cmtimerange/invalid.md) for the `timeRange` parameter.

## See Also

### Creating a player looper

- [- initWithPlayer:templateItem:timeRange:existingItemsOrdering:](<init(player_templateitem_timerange_existingitemsordering_).md>) — Creates a player looper that continuously plays the full duration of a player item while adhering to the specified ordering of existing items in the queue.
- [- initWithPlayer:templateItem:timeRange:](<init(player_templateitem_timerange_).md>) — Creates a player looper that continuously plays the specified time range of a player item.
