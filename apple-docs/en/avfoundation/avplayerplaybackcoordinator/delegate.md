---
title: delegate
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerplaybackcoordinator/delegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinator/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerplaybackcoordinator/delegate.json'
content_hash: 'sha256:23313a43677eef69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerPlaybackCoordinator](../avplayerplaybackcoordinator.md)

# delegate

<sub>Instance Property</sub>

A delegate object for the playback coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVPlayerPlaybackCoordinatorDelegate)? { get set }
```

## See Also

### Configuring the delegate

- [AVPlayerPlaybackCoordinatorDelegate](../avplayerplaybackcoordinatordelegate.md) — A protocol that defines the methods to implement to participate in playback coordination.
