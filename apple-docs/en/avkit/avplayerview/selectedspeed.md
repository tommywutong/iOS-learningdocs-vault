---
title: selectedSpeed
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/selectedspeed
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/selectedspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/selectedspeed.json'
content_hash: 'sha256:50bf989d6f5ae3dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# selectedSpeed

<sub>Instance Property</sub>

The currently selected playback speed.

<sub>macOS</sub>

```swift
var selectedSpeed: AVPlaybackSpeed? { get }
```

## Discussion

This value reflects the associated player’s [defaultRate](../../avfoundation/avplayer/defaultrate.md) property value. If you set the [defaultRate](../../avfoundation/avplayer/defaultrate.md) to a value that doesn’t match a speed contained in the [speeds](speeds.md) property, the system sets this value to `nil`.

## See Also

### Configuring the playback speed

- [speeds](speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [- selectSpeed:](<selectspeed(__).md>) — Selects a specified playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
