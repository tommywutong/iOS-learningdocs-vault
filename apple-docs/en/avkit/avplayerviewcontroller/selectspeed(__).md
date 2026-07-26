---
title: 'selectSpeed(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontroller/selectspeed(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontroller/selectspeed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontroller/selectspeed%28_%3A%29.json'
content_hash: 'sha256:fbf994e2af3c7ae6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewController](../avplayerviewcontroller.md)

# selectSpeed(_:)

<sub>Instance Method</sub>

Selects a specified playback speed.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func selectSpeed(_ speed: AVPlaybackSpeed)
```

## Parameters

- `speed` — The playback speed to select.

## Discussion

If you call this method with a speed that isn’t contained in the [speeds](speeds.md) property, the system ignores the call.

## See Also

### Configuring playback speed

- [speeds](speeds.md) — A list of user-selectable playback speeds to show in the playback speed control.
- [selectedSpeed](selectedspeed.md) — The currently selected playback speed.
- [AVPlaybackSpeed](../avplaybackspeed.md) — An object that represents a user-selectable playback speed in a playback user interface.
