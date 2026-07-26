---
title: 'playerView(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewdelegate/playerview(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewdelegate/playerview%28_%3Arestoreuserinterfaceforfullscreenexitwithcompletionhandler%3A%29.json'
content_hash: 'sha256:7754406293cc6a75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewDelegate](../avplayerviewdelegate.md)

# playerView(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

<sub>Instance Method</sub>

Tells the delegate to restore the app’s user interface when exiting full-screen mode.

<sub>macOS</sub>

```swift
optional func playerView(_ playerView: AVPlayerView, restoreUserInterfaceForFullScreenExitWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>macOS</sub>

```swift
optional func playerViewRestoreUserInterfaceForFullScreenExit(_ playerView: AVPlayerView) async -> Bool
```

## Parameters

- `playerView` — The player view.

- `completionHandler` — You must call the completion handler with a value of `true` to allow the system to finish restoring your app’s user interface.

## See Also

### Responding to Full Screen Events

- [- playerViewWillEnterFullScreen:](<playerviewwillenterfullscreen(__).md>) — Tells the delegate that the player view is about to enter full-screen mode.
- [- playerViewDidEnterFullScreen:](<playerviewdidenterfullscreen(__).md>) — Tells the delegate that the player view entered full-screen mode.
- [- playerViewWillExitFullScreen:](<playerviewwillexitfullscreen(__).md>) — Tells the delegate that the player view is about to exit full-screen mode.
- [- playerViewDidExitFullScreen:](<playerviewdidexitfullscreen(__).md>) — Tells the delegate that the player view exited full-screen mode.
