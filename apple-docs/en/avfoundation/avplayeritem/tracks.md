---
title: tracks
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/tracks
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/tracks'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/tracks.json'
content_hash: 'sha256:340455913edd9b6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# tracks

<sub>Instance Property</sub>

An array of player item track objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated var tracks: [AVPlayerItemTrack] { get }
```

## Discussion

The value is an empty array before the player loads the underlying tracks. Key-value observe this property value to access valid tracks as soon as they’re available.
