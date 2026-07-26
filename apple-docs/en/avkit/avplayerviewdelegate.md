---
title: AVPlayerViewDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewdelegate
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewdelegate.json'
content_hash: 'sha256:faaf8a020e64939e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewDelegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to participate in the player view’s full-screen presentation life cycle.

<sub>macOS</sub>

```swift
protocol AVPlayerViewDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Full Screen Events

- [- playerViewWillEnterFullScreen:](<avplayerviewdelegate/playerviewwillenterfullscreen(__).md>) — Tells the delegate that the player view is about to enter full-screen mode.
- [- playerViewDidEnterFullScreen:](<avplayerviewdelegate/playerviewdidenterfullscreen(__).md>) — Tells the delegate that the player view entered full-screen mode.
- [- playerViewWillExitFullScreen:](<avplayerviewdelegate/playerviewwillexitfullscreen(__).md>) — Tells the delegate that the player view is about to exit full-screen mode.
- [- playerViewDidExitFullScreen:](<avplayerviewdelegate/playerviewdidexitfullscreen(__).md>) — Tells the delegate that the player view exited full-screen mode.
- [- playerView:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<avplayerviewdelegate/playerview(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface when exiting full-screen mode.

## See Also

### Setting the delegate object

- [delegate](avplayerview/delegate.md) — The player view’s delegate object.
