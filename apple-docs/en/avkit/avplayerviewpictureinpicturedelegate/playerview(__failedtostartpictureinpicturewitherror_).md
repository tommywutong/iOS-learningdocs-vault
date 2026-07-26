---
title: 'playerView(_:failedToStartPictureInPictureWithError:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:failedtostartpictureinpicturewitherror:)'
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview(_:failedtostartpictureinpicturewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate/playerview%28_%3Afailedtostartpictureinpicturewitherror%3A%29.json'
content_hash: 'sha256:5419da811e9c1e2f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPlayerViewPictureInPictureDelegate](../avplayerviewpictureinpicturedelegate.md)

# playerView(_:failedToStartPictureInPictureWithError:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture playback failed to start.

<sub>macOS</sub>

```swift
optional func playerView(_ playerView: AVPlayerView, failedToStartPictureInPictureWithError error: any Error)
```

## Parameters

- `playerView` — The player view.

- `error` — An error object describing the failure.

## See Also

### Responding to Picture in Picture Playback Events

- [- playerViewWillStartPictureInPicture:](<playerviewwillstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to start.
- [- playerViewDidStartPictureInPicture:](<playerviewdidstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback started.
- [- playerViewWillStopPictureInPicture:](<playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<playerview(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [- playerViewShouldAutomaticallyDismissAtPictureInPictureStart:](<playerviewshouldautomaticallydismissatpicture(inpicturestart_).md>) — Asks the delegate if the player view should miniaturize when Picture in Picture starts.
