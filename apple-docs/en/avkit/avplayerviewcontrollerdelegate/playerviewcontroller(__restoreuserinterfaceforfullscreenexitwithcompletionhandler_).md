---
title: 'playerViewController(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforfullscreenexitwithcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Arestoreuserinterfaceforfullscreenexitwithcompletionhandler%3A%29.json'
content_hash: 'sha256:9faf9a8c503e4db8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:restoreUserInterfaceForFullScreenExitWithCompletionHandler:)

<sub>Instance Method</sub>

Tells the delegate to restore the app’s user interface after returning from a full-screen presentation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForFullScreenExitWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
optional func playerViewControllerRestoreUserInterfaceForFullScreenExit(_ playerViewController: AVPlayerViewController) async -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

- `completionHandler` — The completion handler to call for the system to finish restoring your user interface. You must invoke this callback with a value of `true`.

## See Also

### Responding to Full-Screen Presentations

- [- playerViewController:willBeginFullScreenPresentationWithAnimationCoordinator:](<playerviewcontroller(__willbeginfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to start full-screen display.
- [- playerViewController:willEndFullScreenPresentationWithAnimationCoordinator:](<playerviewcontroller(__willendfullscreenpresentationwithanimationcoordinator_).md>) — Tells the delegate when the player view controller is about to end full-screen display.
