---
title: isPictureInPicturePossible
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/ispictureinpicturepossible
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturepossible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturepossible.json'
content_hash: 'sha256:d91bd7916ed1a903'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# isPictureInPicturePossible

<sub>Instance Property</sub>

A Boolean value that indicates whether Picture in Picture playback is currently possible.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPictureInPicturePossible: Bool { get }
```

## Discussion

This property value is `false` if another app, like FaceTime, is presenting Picture in Picture content.

This property is key-value observable.

## See Also

### Accessing Picture in Picture State

- [+ isPictureInPictureSupported](<ispictureinpicturesupported().md>) — Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [pictureInPictureActive](ispictureinpictureactive.md) — A Boolean value that indicates whether the Picture in Picture window is onscreen.
- [pictureInPictureSuspended](ispictureinpicturesuspended.md) — A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.
