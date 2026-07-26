---
title: 'playerViewControllerWillStartPictureInPicture(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontrollerwillstartpictureinpicture%28_%3A%29.json'
content_hash: 'sha256:87c39d71ec89e854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewControllerWillStartPictureInPicture(_:)

<sub>Instance Method</sub>

Tells the delegate when Picture in Picture is about to start.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewControllerWillStartPictureInPicture(_ playerViewController: AVPlayerViewController)
```

## Parameters

- `playerViewController` — The player view controller.

## Discussion

Implement this method to update your player user interface, such as hiding or disabling playback controls, prior to PiP starting.

## See Also

### Responding to Picture in Picture Life Cycle Events

- [- playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(__).md>) — Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [- playerViewControllerDidStartPictureInPicture:](<playerviewcontrollerdidstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture starts.
- [- playerViewController:failedToStartPictureInPictureWithError:](<playerviewcontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate when Picture in Picture fails to start.
- [- playerViewControllerWillStopPictureInPicture:](<playerviewcontrollerwillstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to stop.
- [- playerViewControllerDidStopPictureInPicture:](<playerviewcontrollerdidstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture stops.
- [- playerViewController:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerviewcontroller(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.
