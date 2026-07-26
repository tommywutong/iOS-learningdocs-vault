---
title: 'playerWithURL:'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/playerwithurl:'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/playerwithurl:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/playerwithurl%3A.json'
content_hash: 'sha256:86430a810527f1d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# playerWithURL:

<sub>Type Method</sub>

Returns a new player to play a single audiovisual resource referenced by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) playerWithURL:(NSURL *) URL;
```

## Parameters

- `URL` — A URL that identifies an audiovisual resource.

## Return Value

A new player initialized to play the audiovisual resource specified by `URL`.

## Discussion

This method implicitly creates an [AVPlayerItem](../avplayeritem.md) object. You can get the player item using [currentItem](currentitem.md).

## See Also

### Creating a player

- [- initWithURL:](<init(url_)-87cxx.md>) — Creates a new player to play a single audiovisual resource referenced by a given URL.
- [playerWithPlayerItem:](playerwithplayeritem_.md) — Returns a new player initialized to play the specified player item.
- [- initWithPlayerItem:](<init(playeritem_).md>) — Creates a new player to play the specified player item.
- [- init](<init().md>) — Creates a player object.
