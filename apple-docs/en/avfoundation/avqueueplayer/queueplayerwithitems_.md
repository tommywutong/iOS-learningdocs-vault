---
title: 'queuePlayerWithItems:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avqueueplayer/queueplayerwithitems:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueueplayer/queueplayerwithitems:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueueplayer/queueplayerwithitems%3A.json'
content_hash: 'sha256:818086140db0a3a0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuePlayer](../avqueueplayer.md)

# queuePlayerWithItems:

<sub>Type Method</sub>

Returns an object that plays a queue of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) queuePlayerWithItems:(NSArray<AVPlayerItem *> *) items;
```

## Parameters

- `items` — An array of [AVPlayerItem](../avplayeritem.md) objects with which to initially populate the player’s queue.

## Return Value

A new queue player.

## See Also

### Creating a queue player

- [- initWithItems:](<init(items_).md>) — Creates an object that plays a queue of items.
