---
title: AVPlayerViewControllerAnimationCoordinator
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [tvOS 11.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewcontrolleranimationcoordinator
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrolleranimationcoordinator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrolleranimationcoordinator.json'
content_hash: 'sha256:630fc62bee9ecb8b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewControllerAnimationCoordinator

<sub>Protocol</sub>

A protocol that defines the methods to implement to synchronize animations with playback controls’ visibility animation.

<sub>tvOS</sub>

```swift
protocol AVPlayerViewControllerAnimationCoordinator : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Coordinating Animations

- [- addCoordinatedAnimations:completion:](<avplayerviewcontrolleranimationcoordinator/addcoordinatedanimations(__completion_).md>) — Adds animations to perform alongside the playback controls’ visibility animation.

## See Also

### Responding to Transport Bar Changes

- [- playerViewController:willTransitionToVisibilityOfTransportBar:withAnimationCoordinator:](<avplayerviewcontrollerdelegate/playerviewcontroller(__willtransitiontovisibilityoftransportbar_with_).md>) — Tells the delegate when the transport bar’s visibility is about to change.
