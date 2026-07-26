---
title: 'playerViewController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewcontrollerdelegate/playerviewcontroller%28_%3Arestoreuserinterfaceforpictureinpicturestopwithcompletionhandler%3A%29.json'
content_hash: 'sha256:320574cf340465f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewControllerDelegate](../avplayerviewcontrollerdelegate.md)

# playerViewController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

<sub>Instance Method</sub>

Tells the delegate when Picture in Picture is about to stop so you can restore your app’s user interface.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewController(_ playerViewController: AVPlayerViewController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func playerViewControllerRestoreUserInterfaceForPictureInPictureStop(_ playerViewController: AVPlayerViewController) async -> Bool
```

## Parameters

- `playerViewController` — The player view controller.

- `completionHandler` — You must call the completion handler with a value of `true` to allow the system to finish restoring your app’s user interface.

## Discussion

Implement this method to reestablish your playback user interface when PiP ends. The framework calls this method no matter how PiP ends, whether it’s because the user ended playback, the user tapped the button to return ongoing video playback to your app, or the video finished playing on its own.

## See Also

### Responding to Picture in Picture Life Cycle Events

- [- playerViewControllerShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewcontrollershouldautomaticallydismissatpictureinpicturestart(__).md>) — Asks the delegate whether the player view controller automatically dismisses itself when Picture in Picture starts.
- [- playerViewControllerWillStartPictureInPicture:](<playerviewcontrollerwillstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to start.
- [- playerViewControllerDidStartPictureInPicture:](<playerviewcontrollerdidstartpictureinpicture(__).md>) — Tells the delegate when Picture in Picture starts.
- [- playerViewController:failedToStartPictureInPictureWithError:](<playerviewcontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate when Picture in Picture fails to start.
- [- playerViewControllerWillStopPictureInPicture:](<playerviewcontrollerwillstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture is about to stop.
- [- playerViewControllerDidStopPictureInPicture:](<playerviewcontrollerdidstoppictureinpicture(__).md>) — Tells the delegate when Picture in Picture stops.
