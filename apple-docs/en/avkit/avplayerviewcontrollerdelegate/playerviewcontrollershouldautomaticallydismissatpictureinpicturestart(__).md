---
title: 'playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollershouldautomaticallydismissatpictureinpicturestart%28_%3A%29.json'
content_hash: 'sha256:aac94b0636606736'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_:)

<sub>Instance Method</sub>

Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart(_ playerViewController: AVPlayerViewController) -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

## Return Value

`true` to indicate that the player view controller automatically dismisses itself; otherwise `false`.

## Discussion

Implement this method and return `false` to prevent the player view controller from automatically dismissing when Picture in Picture starts.

## See Also

### Responding to Picture in Picture Life Cycle Events

- [- playerViewControllerWillStartPictureInPicture:](<playerviewcontrollerwillstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to start.
- [- playerViewControllerDidStartPictureInPicture:](<playerviewcontrollerdidstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture starts.
- [- playerViewController:failedToStartPictureInPictureWithError:](<playerviewcontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate when Picture in Picture fails to start.
- [- playerViewControllerWillStopPictureInPicture:](<playerviewcontrollerwillstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to stop.
- [- playerViewControllerDidStopPictureInPicture:](<playerviewcontrollerdidstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture stops.
- [- playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.
