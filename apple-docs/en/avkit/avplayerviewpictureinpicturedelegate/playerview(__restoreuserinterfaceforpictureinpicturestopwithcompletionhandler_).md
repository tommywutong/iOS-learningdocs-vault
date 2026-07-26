---
title: 'playerView(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview%28_%3Arestoreuserinterfaceforpictureinpicturestopwithcompletionhandler%3A%29.json'
content_hash: 'sha256:e5cd7707683798bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)

# playerView(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

<sub>Instance Method</sub>

Tells the delegate to restore the user interface before Picture in Picture playback stops.

<sub>macOS</sub>

```swift
optional func playerView(_ playerView: AVPlayerView, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>macOS</sub>

```swift
optional func playerViewRestoreUserInterfaceForPictureInPictureStop(_ playerView: AVPlayerView) async -> Bool
```

## Parameters

- `playerView` — The player view.

- `completionHandler` — The completion handler to call after you’ve restored the user interface.

## See Also

### Responding to Picture in Picture Playback Events

- [- playerViewWillStartPictureInPicture:](<playerviewwillstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to start.
- [- playerViewDidStartPictureInPicture:](<playerviewdidstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback started.
- [- playerViewWillStopPictureInPicture:](<playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:failedToStartPictureInPictureWithError:](<playerview(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture playback failed to start.
- [- playerViewShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewshouldautomaticallydismissatpicture(inpicturestart_).md>) — Asks the delegate if the player view should miniaturize when Picture in Picture starts.
