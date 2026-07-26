---
title: speeds
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerview/speeds
source_url: 'https://developer.apple.com/documentation/avkit/avplayerview/speeds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerview/speeds.json'
content_hash: 'sha256:df36a3b80f64fde5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerView](../avplayerview.md)

# speeds

<sub>Instance Property</sub>

A list of user-selectable playback speeds to show in the playback speed control.

<sub>macOS</sub>

```swift
var speeds: [AVPlaybackSpeed] { get set }
```

## Discussion

By default, this property value equals [systemDefaultSpeeds](../avplaybackspeed/systemdefaultspeeds.md). Setting this property to an empty array hides the playback speed selection user interface.

To set the playback speed programmatically, call the [- selectSpeed:](<selectspeed(__).md>) method, or set the value of the [defaultRate](../../avfoundation/avplayer/defaultrate.md) property on the view controller’s associated [AVPlayer](../../avfoundation/avplayer.md) object.

## See Also

### Configuring the playback speed

- [selectedSpeed](selectedspeed.md) — The currently selected playback speed.
- [- selectSpeed:](<selectspeed(__).md>) — Selects a specified playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
