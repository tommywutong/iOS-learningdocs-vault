---
title: 'init(player:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avplayerlayer/init(player:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlayer/init(player:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlayer/init%28player%3A%29.json'
content_hash: 'sha256:ecba060cdfbe45df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLayer](../avplayerlayer.md)

# init(player:)

<sub>Initializer</sub>

Creates a layer object to present the visual contents of a player’s current item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(player: AVPlayer?)
```

## Parameters

- `player` — The player whose visual contents the layer presents.

## Return Value

A layer that displays the visual output of the associated player.

## Discussion

You may create an arbitrary number of layers for the same player object.
