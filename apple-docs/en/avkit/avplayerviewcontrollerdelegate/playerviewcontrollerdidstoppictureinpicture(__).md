---
title: 'playerViewControllerDidStopPictureInPicture(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerdidstoppictureinpicture%28_%3A%29.json'
content_hash: 'sha256:6c86f8a4f3a9d71f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerDidStopPictureInPicture(_:)

<sub>Instance Method</sub>

Tells the delegate when Picture in Picture stops.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewControllerDidStopPictureInPicture(_ playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController` — The player view controller.

## Discussion

Don’t restore your app’s user interface in your implementation of this method. Instead, do it in the [- playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) method.

## See Also

### Responding to Picture in Picture Life Cycle Events

- [- playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(__).md>) — Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [- playerViewControllerWillStartPictureInPicture:](<playerviewcontrollerwillstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to start.
- [- playerViewControllerDidStartPictureInPicture:](<playerviewcontrollerdidstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture starts.
- [- playerViewController:failedToStartPictureInPictureWithError:](<playerviewcontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate when Picture in Picture fails to start.
- [- playerViewControllerWillStopPictureInPicture:](<playerviewcontrollerwillstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to stop.
- [- playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.
