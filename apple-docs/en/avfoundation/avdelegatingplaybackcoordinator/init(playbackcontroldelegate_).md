---
title: 'init(playbackControlDelegate:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avdelegatingplaybackcoordinator/init(playbackcontroldelegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avdelegatingplaybackcoordinator/init(playbackcontroldelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avdelegatingplaybackcoordinator/init%28playbackcontroldelegate%3A%29.json'
content_hash: 'sha256:add951d728cabc72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVDelegatingPlaybackCoordinator](../avdelegatingplaybackcoordinator.md)

# init(playbackControlDelegate:)

<sub>Initializer</sub>

Creates a playback coordinator for a custom playback object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(playbackControlDelegate: any AVPlaybackCoordinatorPlaybackControlDelegate)
```

## Parameters

- `playbackControlDelegate` — The playback control delegate for the playback coordinator.

## Discussion

If your app doesn’t use [AVPlayer](../avplayer.md) for playback, create an instance of this class to coordinate playback of your customer player.

## See Also

### Creating a coordinator

- [AVPlaybackCoordinatorPlaybackControlDelegate](../avplaybackcoordinatorplaybackcontroldelegate.md) — A protocol that defines the method to implement to respond to playback commands from the playback coordinator.
