---
title: 'playerViewDidExitFullScreen(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewdelegate/playerviewdidexitfullscreen(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerviewdidexitfullscreen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewdelegate/playerviewdidexitfullscreen%28_%3A%29.json'
content_hash: 'sha256:dda471c000da8860'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewDelegate](../avplayerviewdelegate.md)

# playerViewDidExitFullScreen(_:)

<sub>Instance Method</sub>

Tells the delegate that the player view exited full-screen mode.

<sub>macOS</sub>

```swift
optional func playerViewDidExitFullScreen(_ playerView: AVPlayerView)
```

## Parameters

- `playerView` — The player view.

## See Also

### Responding to Full Screen Events

- [- playerViewWillEnterFullScreen:](<playerviewwillenterfullscreen(__).md>) — Tells the delegate that the player view is about to enter full-screen mode.
- [- playerViewDidEnterFullScreen:](<playerviewdidenterfullscreen(__).md>) — Tells the delegate that the player view entered full-screen mode.
- [- playerViewWillExitFullScreen:](<playerviewwillexitfullscreen(__).md>) — Tells the delegate that the player view is about to exit full-screen mode.
- [- playerView:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<playerview(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface when exiting full-screen mode.
