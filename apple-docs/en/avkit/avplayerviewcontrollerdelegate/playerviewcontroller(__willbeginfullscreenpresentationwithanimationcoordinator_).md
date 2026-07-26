---
title: 'playerViewController(_:willBeginFullScreenPresentationWithAnimationCoordinator:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:willbeginfullscreenpresentationwithanimationcoordinator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Awillbeginfullscreenpresentationwithanimationcoordinator%3A%29.json'
content_hash: 'sha256:43dede614dceeade'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:willBeginFullScreenPresentationWithAnimationCoordinator:)

<sub>Instance Method</sub>

Tells the delegate when the player view controller is about to start full-screen display.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, willBeginFullScreenPresentationWithAnimationCoordinator coordinator: any UIViewControllerTransitionCoordinator)
```

## Parameters

- `playerViewController` — The player view controller.

- `coordinator` — The transition coordinator to use when coordinating animations.

## Discussion

This method isn’t called if you embed the player view controller as a child of the presented view controller.

## See Also

### Responding to Full-Screen Presentations

- [- playerViewController:willEndFullScreenPresentationWithAnimationCoordinator:](<playerviewcontroller(__willendfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to end full-screen display.
- [- playerViewController:restoreUserInterfaceForFullScreenExitWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforfullscreenexitwithcompletionhandler_).md>) — Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.
