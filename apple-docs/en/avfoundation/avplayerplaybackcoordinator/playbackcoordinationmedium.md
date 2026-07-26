---
title: playbackCoordinationMedium
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerplaybackcoordinator/playbackcoordinationmedium
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/playbackcoordinationmedium'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerplaybackcoordinator/playbackcoordinationmedium.json'
content_hash: 'sha256:589cc48069744476'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerPlaybackCoordinator](../avplayerplaybackcoordinator.md)

# playbackCoordinationMedium

<sub>Instance Property</sub>

The AVPlaybackCoordinationMedium this playback coordinator is connected to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var playbackCoordinationMedium: AVPlaybackCoordinationMedium? { get }
```

## Discussion

This is the AVPlaybackCoordinationMedium the playback coordinator is connected to. If not NULL, the playback coordinator is connected to the specified coordination medium. The playback coordinator is not available to coordinate with a group session. If NULL, the playback coordinator is not connected to any playback coordination medium. The playback coordinator is available to coordinate with a group session through the `coordinateWithSession` API.

## See Also

### Managing coordination

- [- coordinateUsingCoordinationMedium:error:](<coordinate(using_).md>) — Connects the playback coordinator to the coordination medium
