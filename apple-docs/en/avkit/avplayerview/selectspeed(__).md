---
title: 'selectSpeed(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerview/selectspeed(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/selectspeed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/selectspeed%28_%3A%29.json'
content_hash: 'sha256:168170bf07c0fb8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# selectSpeed(_:)

<sub>Instance Method</sub>

Selects a specified playback speed.

<sub>macOS</sub>

```swift
func selectSpeed(_ speed: AVPlaybackSpeed)
```

## Parameters

- `speed` — The playback speed to select.

## Discussion

If you call this method with a speed that isn’t contained in the [speeds](speeds.md) property, the system ignores the call.

## See Also

### Configuring the playback speed

- [speeds](speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [selectedSpeed](selectedspeed.md) — The currently selected playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
