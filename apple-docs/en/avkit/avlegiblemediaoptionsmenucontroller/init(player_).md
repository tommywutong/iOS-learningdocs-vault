---
title: 'init(player:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 26.4+, iPadOS 26.4+, Mac Catalyst 26.4+, macOS 26.4+, visionOS 26.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avlegiblemediaoptionsmenucontroller/init(player:)'
source_url: 'https://developer.apple.com/documentation/avkit/avlegiblemediaoptionsmenucontroller/init(player:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avlegiblemediaoptionsmenucontroller/init%28player%3A%29.json'
content_hash: 'sha256:1deeeaa28a366b3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVLegibleMediaOptionsMenuController](../avlegiblemediaoptionsmenucontroller.md)

# init(player:)

<sub>Initializer</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
init(player: AVPlayer?)
```

## Parameters

- `player` — The AVPlayer to build menus from, or nil for non-track-specific options only

## Discussion

Creates an AVLegibleMediaOptionsMenuController with an optional player

When player is non-nil, both media tracks and caption appearance options will be included, otherwise, only caption appearance options.
