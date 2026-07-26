---
title: AVPlayerViewPictureInPictureDelegate
framework: AVKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [macOS 10.15+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avplayerviewpictureinpicturedelegate
source_url: 'https://developer.apple.com/documentation/avkit/avplayerviewpictureinpicturedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avplayerviewpictureinpicturedelegate.json'
content_hash: 'sha256:e4fc67b596d7d287'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPlayerViewPictureInPictureDelegate

<sub>Protocol</sub>

A protocol that defines the methods to implement to respond to Picture in Picture playback events.

<sub>macOS</sub>

```swift
protocol AVPlayerViewPictureInPictureDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Responding to Picture in Picture Playback Events

- [- playerViewWillStartPictureInPicture:](<avplayerviewpictureinpicturedelegate/playerviewwillstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to start.
- [- playerViewDidStartPictureInPicture:](<avplayerviewpictureinpicturedelegate/playerviewdidstartpicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback started.
- [- playerViewWillStopPictureInPicture:](<avplayerviewpictureinpicturedelegate/playerviewwillstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback is about to stop.
- [- playerViewDidStopPictureInPicture:](<avplayerviewpictureinpicturedelegate/playerviewdidstoppicture(inpicture_).md>) — Tells the delegate that Picture in Picture playback stopped.
- [- playerView:failedToStartPictureInPictureWithError:](<avplayerviewpictureinpicturedelegate/playerview(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture playback failed to start.
- [- playerView:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:](<avplayerviewpictureinpicturedelegate/playerview(__restoreuserinterfaceforpictureinpicturestopwithcompletionhandler_).md>) — Tells the delegate to restore the user interface before Picture in Picture playback stops.
- [- playerViewShouldAutomaticallyDismissAtPictureInPictureStart:](<avplayerviewpictureinpicturedelegate/playerviewshouldautomaticallydismissatpicture(inpicturestart_).md>) — Asks the delegate if the player view should miniaturize when Picture in Picture starts.

## See Also

### Configuring picture in picture

- [allowsPictureInPicturePlayback](avplayerview/allowspictureinpictureplayback.md) — A Boolean value that determines whether the player view allows Picture in Picture playback.
- [pictureInPictureDelegate](avplayerview/pictureinpicturedelegate.md) — The Picture in Picture delegate object.
