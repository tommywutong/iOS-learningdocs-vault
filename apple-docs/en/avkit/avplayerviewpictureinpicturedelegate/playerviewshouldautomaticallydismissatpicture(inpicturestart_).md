---
title: 'playerViewShouldAutomaticallyDismissAtPicture(inPictureStart:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture%28inpicturestart%3A%29.json'
content_hash: 'sha256:2818483ecdbc7042'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)

# playerViewShouldAutomaticallyDismissAtPicture(inPictureStart:)

<sub>Instance Method</sub>

Asks the delegate if the player view should miniaturize when Picture in Picture starts.

<sub>macOS</sub>

```swift
optional func playerViewShouldAutomaticallyDismissAtPicture(inPictureStart playerView: AVPlayerView) -> Bool
```

## Parameters

- `playerView` — The player view.

## Return Value

`true` if the player view should automatically be miniaturized; otherwise `false`.

## See Also

### Responding to Picture in Picture Playback Events

- [- playerViewWillStartPictureInPicture:](<playerviewwillstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to start.
- [- playerViewDidStartPictureInPicture:](<playerviewdidstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback started.
- [- playerViewWillStopPictureInPicture:](<playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:failedToStartPictureInPictureWithError:](<playerview(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture playback failed to start.
- [- playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerview(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture playback stops.
