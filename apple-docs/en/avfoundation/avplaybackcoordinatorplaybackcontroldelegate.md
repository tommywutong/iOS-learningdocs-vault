---
title: AVPlaybackCoordinatorPlaybackControlDelegate
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate
source_url: 'https://developer.apple.com/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplaybackcoordinatorplaybackcontroldelegate.json'
content_hash: 'sha256:559f5923282d31ee'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlaybackCoordinatorPlaybackControlDelegate

<sub>Protocol</sub>

A protocol that defines the method to implement to respond to playback commands from the playback coordinator.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
protocol AVPlaybackCoordinatorPlaybackControlDelegate : NSObjectProtocol, Sendable
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Responding to commands

- [- playbackCoordinator:didIssuePlayCommand:completionHandler:](<avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(__didissue_completionhandler_)-73p3a.md>) — Tells the delegate to match the playback rate to that of the group when the rate is nonzero.
- [- playbackCoordinator:didIssuePauseCommand:completionHandler:](<avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(__didissue_completionhandler_)-56t01.md>) — Tells the delegate to pause playback.
- [- playbackCoordinator:didIssueSeekCommand:completionHandler:](<avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(__didissue_completionhandler_)-4fk8y.md>) — Tells the delegate to seek to a new time.
- [- playbackCoordinator:didIssueBufferingCommand:completionHandler:](<avplaybackcoordinatorplaybackcontroldelegate/playbackcoordinator(__didissue_completionhandler_)-btle.md>) — Tells the delegate to expect playback soon and to start buffering media data in preparation.

## See Also

### Creating a coordinator

- [- initWithPlaybackControlDelegate:](<avdelegatingplaybackcoordinator/init(playbackcontroldelegate_).md>) — Creates a playback coordinator for a custom playback object.
