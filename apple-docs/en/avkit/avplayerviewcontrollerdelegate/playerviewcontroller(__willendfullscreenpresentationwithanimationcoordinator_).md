---
title: 'playerViewController(_:willEndFullScreenPresentationWithAnimationCoordinator:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willendfullscreenpresentationwithanimationcoordinator:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willendfullscreenpresentationwithanimationcoordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Awillendfullscreenpresentationwithanimationcoordinator%3A%29.json'
content_hash: 'sha256:6a0c6d1ae275e5cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:willEndFullScreenPresentationWithAnimationCoordinator:)

<sub>Instance Method</sub>

Tells the delegate when the player view controller is about to end full-screen display.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willEndFullScreenPresentationWithAnimationCoordinator coordinator: any UIViewControllerTransitionCoordinator)
```

## Parameters

- `playerViewController` — The player view controller.

- `coordinator` — The transition coordinator to use when coordinating animations.

## See Also

### Responding to Full-Screen Presentations

- [- playerViewController:willBeginFullScreenPresentationWithAnimationCoordinator:](<playerviewcontroller(__willbeginfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to start full-screen display.
- [- playerViewController:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.
