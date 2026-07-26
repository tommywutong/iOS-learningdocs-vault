---
title: 'init(playerItem:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayer/init(playeritem:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/init(playeritem:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/init%28playeritem%3A%29.json'
content_hash: 'sha256:bf03d0b36fed452b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# init(playerItem:)

<sub>Initializer</sub>

Creates a new player to play the specified player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(playerItem item: AVPlayerItem?)
```

## Parameters

- `item` — The player item to play.

## Return Value

A new player initialized to play `item`.

## See Also

### Creating a player

- [- initWithURL:](<init(url_)-87cxx.md>) — Creates a new player to play a single audiovisual resource referenced by a given URL.
- [- init](<init().md>) — Creates a player object.
