---
title: 'playerViewDidStartPicture(inPicture:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate/playerviewdidstartpicture%28inpicture%3A%29.json'
content_hash: 'sha256:093ff7d742005165'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)

# playerViewDidStartPicture(inPicture:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture playback started.

<sub>macOS</sub>

```swift
optional func playerViewDidStartPicture(inPicture playerView: AVPlayerView)
```

## Parameters

- `playerView` — The player view.

## See Also

### Responding to Picture in Picture Playback Events

- [- playerViewWillStartPictureInPicture:](<playerviewwillstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to start.
- [- playerViewWillStopPictureInPicture:](<playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:failedToStartPictureInPictureWithError:](<playerview(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture playback failed to start.
- [- playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerview(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [- playerViewShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewshouldautomaticallydismissatpicture(inpicturestart_).md>) — Asks the delegate if the player view should miniaturize when Picture in Picture starts.
