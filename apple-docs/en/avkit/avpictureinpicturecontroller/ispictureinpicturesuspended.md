---
title: isPictureInPictureSuspended
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesuspended
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesuspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesuspended.json'
content_hash: 'sha256:61623e42d9eea145'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# isPictureInPictureSuspended

<sub>Instance Property</sub>

A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPictureInPictureSuspended: Bool { get }
```

## Discussion

The system suspends your app’s Picture in Picture session when another app, typically FaceTime, is using the feature. In this state, your video playback is active but paused and offscreen. Picture in Picture resumes automatically when the other app finishes using PiP.

## See Also

### Accessing Picture in Picture State

- [+ isPictureInPictureSupported](<ispictureinpicturesupported().md>) — Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [pictureInPicturePossible](ispictureinpicturepossible.md) — A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [pictureInPictureActive](ispictureinpictureactive.md) — A Boolean value that indicates whether the Picture in Picture window is onscreen.
