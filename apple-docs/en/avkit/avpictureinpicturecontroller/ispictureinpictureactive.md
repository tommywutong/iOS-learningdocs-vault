---
title: isPictureInPictureActive
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/ispictureinpictureactive
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpictureactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/ispictureinpictureactive.json'
content_hash: 'sha256:f5cb23761c3c2166'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# isPictureInPictureActive

<sub>Instance Property</sub>

A Boolean value that indicates whether the Picture in Picture window is onscreen.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isPictureInPictureActive: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Accessing Picture in Picture State

- [+ isPictureInPictureSupported](<ispictureinpicturesupported().md>) — Returns a Boolean value that indicates whether the current device supports Picture in Picture.
- [pictureInPicturePossible](ispictureinpicturepossible.md) — A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [pictureInPictureSuspended](ispictureinpicturesuspended.md) — A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.
