---
title: 'init(url:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/init(url:)-87cxx'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/init(url:)-87cxx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/init%28url%3A%29-87cxx.json'
content_hash: 'sha256:7985f483776bb923'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# init(url:)

<sub>Initializer</sub>

Creates a new player to play a single audiovisual resource referenced by a given URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(url URL: URL)
```

## Parameters

- `URL` — A URL that identifies an audiovisual resource.

## Return Value

A new player instance initialized to play the audiovisual resource specified by `URL`.

## Discussion

This method implicitly creates an [AVPlayerItem](../avplayeritem.md) object. You can get the player item using [currentItem](currentitem.md).

## See Also

### Creating a player

- [- initWithPlayerItem:](<init(playeritem_).md>) — Creates a new player to play the specified player item.
- [- init](<init().md>) — Creates a player object.
