---
title: 'playerViewWillEnterFullScreen(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewdelegate/playerviewwillenterfullscreen(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerviewwillenterfullscreen(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewdelegate/playerviewwillenterfullscreen%28_%3A%29.json'
content_hash: 'sha256:5459abf8fdf1ccc9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewDelegate](../avplayerviewdelegate.md)

# playerViewWillEnterFullScreen(_:)

<sub>Instance Method</sub>

Tells the delegate that the player view is about to enter full-screen mode.

<sub>macOS</sub>

```swift
optional func playerViewWillEnterFullScreen(_ playerView: AVPlayerView)
```

## Parameters

- `playerView` — The player view.

## See Also

### Responding to Full Screen Events

- [- playerViewDidEnterFullScreen:](<playerviewdidenterfullscreen(__).md>) — Tells the delegate that the player view entered full-screen mode.
- [- playerViewWillExitFullScreen:](<playerviewwillexitfullscreen(__).md>) — Tells the delegate that the player view is about to exit full-screen mode.
- [- playerViewDidExitFullScreen:](<playerviewdidexitfullscreen(__).md>) — Tells the delegate that the player view exited full-screen mode.
- [- playerView:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<playerview(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface when exiting full-screen mode.
