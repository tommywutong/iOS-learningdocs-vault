---
title: 'playerViewWillExitFullScreen(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewdelegate/playerviewwillexitfullscreen(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerviewwillexitfullscreen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewdelegate/playerviewwillexitfullscreen%28_%3A%29.json'
content_hash: 'sha256:d1bd1e38d14532a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewDelegate](../avplayerviewdelegate.md)

# playerViewWillExitFullScreen(_:)

<sub>Instance Method</sub>

Tells the delegate that the player view is about to exit full-screen mode.

<sub>macOS</sub>

```swift
optional func playerViewWillExitFullScreen(_ playerView: AVPlayerView)
```

## Parameters

- `playerView` — The player view.

## See Also

### Responding to Full Screen Events

- [- playerViewWillEnterFullScreen:](<playerviewwillenterfullscreen(__).md>) — Tells the delegate that the player view is about to enter full-screen mode.
- [- playerViewDidEnterFullScreen:](<playerviewdidenterfullscreen(__).md>) — Tells the delegate that the player view entered full-screen mode.
- [- playerViewDidExitFullScreen:](<playerviewdidexitfullscreen(__).md>) — Tells the delegate that the player view exited full-screen mode.
- [- playerView:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<playerview(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface when exiting full-screen mode.
