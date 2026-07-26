---
title: speeds
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontroller/speeds
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/speeds'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/speeds.json'
content_hash: 'sha256:2202d30a3a77f005'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# speeds

<sub>Instance Property</sub>

A list of user-selectable playback speeds to show in the playback speed control.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var speeds: [AVPlaybackSpeed] { get set }
```

## Discussion

By default, this property value equals [systemDefaultSpeeds](../avplaybackspeed/systemdefaultspeeds.md). Setting this property to an empty array hides the playback speed selection user interface.

To set the playback speed programmatically, call the [- selectSpeed:](<selectspeed(__).md>) method, or set the value of the [defaultRate](../../avfoundation/avplayer/defaultrate.md) property on the view controller’s associated player object.

## See Also

### Configuring playback speed

- [selectedSpeed](selectedspeed.md) — The currently selected playback speed.
- [- selectSpeed:](<selectspeed(__).md>) — Selects a specified playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
