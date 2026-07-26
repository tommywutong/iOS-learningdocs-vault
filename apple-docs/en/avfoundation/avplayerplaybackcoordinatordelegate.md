---
title: AVPlayerPlaybackCoordinatorDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerplaybackcoordinatordelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerplaybackcoordinatordelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerplaybackcoordinatordelegate.json'
content_hash: 'sha256:678152aeaae0dd95'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerPlaybackCoordinatorDelegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to participate in playback coordination.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVPlayerPlaybackCoordinatorDelegate : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Identifying items

- [- playbackCoordinator:identifierForPlayerItem:](<avplayerplaybackcoordinatordelegate/playbackcoordinator(__identifierfor_).md>) — Returns an identifier for a player item.

### Retrieving interstitial time ranges

- [- playbackCoordinator:interstitialTimeRangesForPlayerItem:](<avplayerplaybackcoordinatordelegate/playbackcoordinator(__interstitialtimerangesfor_).md>) — Asks the delegate for time ranges in a player item that don’t correspond to the primary content.

## See Also

### Configuring the delegate

- [delegate](avplayerplaybackcoordinator/delegate.md) — A delegate object for the playback coordinator.
