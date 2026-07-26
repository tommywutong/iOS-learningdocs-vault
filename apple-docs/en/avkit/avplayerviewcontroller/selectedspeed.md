---
title: selectedSpeed
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/selectedspeed
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/selectedspeed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/selectedspeed.json'
content_hash: 'sha256:9cc02e7f766d5f9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# selectedSpeed

<sub>Instance Property</sub>

The currently selected playback speed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var selectedSpeed: AVPlaybackSpeed? { get }
```

## Discussion

This value reflects the associated player’s [defaultRate](../../avfoundation/avplayer/defaultrate.md) property value. If you set the [defaultRate](../../avfoundation/avplayer/defaultrate.md) to a value that doesn’t match a speed contained in the [speeds](speeds.md) property, the system sets this value to `nil`.

## See Also

### Configuring playback speed

- [speeds](speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [- selectSpeed:](<selectspeed(__).md>) — Selects a specified playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
