---
title: AVPlaybackCoordinationMedium
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinationmedium
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinationmedium'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinationmedium.json'
content_hash: 'sha256:2661568f85b2b7e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlaybackCoordinationMedium

<sub>Class</sub>

The AVPlaybackCoordinationMedium passes states and messages between its connected playback coordinators.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlaybackCoordinationMedium
```

## Overview

The coordination medium passes states and messages from one playback coordinator to all other connected playback coordinators to enable coordination of rate changes and seeks. Subclasses of this type that are used from Swift must fulfill the requirements of a Sendable type.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a coordination medium

- [- init](<avplaybackcoordinationmedium/init().md>) — Initializes an AVPlaybackCoordinationMedium

### Managing playback coordinators

- [connectedPlaybackCoordinators](avplaybackcoordinationmedium/connectedplaybackcoordinators.md) — All playback coordinators that are connected to the coordination medium.

## See Also

### SharePlay

- [Destination Video](../visionos/destination-video.md) — Leverage SwiftUI to build an immersive media experience in a multiplatform app.
- [Supporting coordinated media playback](supporting-coordinated-media-playback.md) — Create synchronized media experiences that enable users to watch and listen across devices.
- [AVPlaybackCoordinator](avplaybackcoordinator.md) — An object that coordinates the playback of players in a connected group.
- [AVPlayerPlaybackCoordinator](avplayerplaybackcoordinator.md) — A playback coordinator subclass that coordinates the playback of player objects in a connected group.
- [AVDelegatingPlaybackCoordinator](avdelegatingplaybackcoordinator.md) — A playback coordinator subclass that coordinates the playback of custom player objects in a connected group.
