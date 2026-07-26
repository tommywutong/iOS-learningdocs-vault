---
title: 'init(player:videoOverlay:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avkit/videoplayer/init(player:videooverlay:)'
source_url: 'https://developer.apple.com/documentation/avkit/videoplayer/init(player:videooverlay:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/videoplayer/init%28player%3Avideooverlay%3A%29.json'
content_hash: 'sha256:f65140e27c3577c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [VideoPlayer](../videoplayer.md)

# init(player:videoOverlay:)

<sub>Initializer</sub>

Creates a video-player user interface for the player object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency init(player: AVPlayer?, @ViewBuilder videoOverlay: () -> VideoOverlay)
```

## Parameters

- `player` — The player that plays the audiovisual content.

- `videoOverlay` — A closure that returns a `VideoOverlay` view to present over the player’s video content. This view is fully interactive, but is placed below the system-provided playback controls, and only receives unhandled events.

## See Also

### Creating a video player

- [init(player:)](<init(player_).md>) — Creates a video-player user interface for the player object.
