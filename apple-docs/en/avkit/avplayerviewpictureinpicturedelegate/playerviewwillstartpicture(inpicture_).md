---
title: 'playerViewWillStartPicture(inPicture:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewwillstartpicture%28inpicture%3A%29.json'
content_hash: 'sha256:8889b96e22e4c2ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)

# playerViewWillStartPicture(inPicture:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture playback is about to start.

<sub>macOS</sub>

```swift
optional func playerViewWillStartPicture(inPicture playerView: AVPlayerView)
```

## Parameters

- `playerView` — The player view.

## See Also

### Responding to Picture in Picture Playback Events

- [- playerViewDidStartPictureInPicture:](<playerviewdidstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback started.
- [- playerViewWillStopPictureInPicture:](<playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:failedToStartPictureInPictureWithError:](<playerview(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture playback failed to start.
- [- playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerview(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [- playerViewShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewshouldautomaticallydismissatpicture(inpicturestart_).md>) — Asks the delegate if the player view should miniaturize when Picture in Picture starts.
