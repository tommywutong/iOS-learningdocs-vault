---
title: 'playerWithPlayerItem:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/playerwithplayeritem:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/playerwithplayeritem:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/playerwithplayeritem%3A.json'
content_hash: 'sha256:45f8a31d58c5137c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# playerWithPlayerItem:

<sub>Type Method</sub>

Returns a new player initialized to play the specified player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) playerWithPlayerItem:(AVPlayerItem *) item;
```

## Parameters

- `item` — The player item to play.

## Return Value

A new player initialized to play `item`.

## See Also

### Creating a player

- [playerWithURL:](playerwithurl_.md) — Returns a new player to play a single audiovisual resource referenced by a given URL.
- [- initWithURL:](<init(url_)-87cxx.md>) — Creates a new player to play a single audiovisual resource referenced by a given URL.
- [- initWithPlayerItem:](<init(playeritem_).md>) — Creates a new player to play the specified player item.
- [- init](<init().md>) — Creates a player object.
