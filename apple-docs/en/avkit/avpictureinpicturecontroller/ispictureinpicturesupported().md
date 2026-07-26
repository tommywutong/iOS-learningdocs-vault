---
title: isPictureInPictureSupported()
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesupported()
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesupported()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/ispictureinpicturesupported%28%29.json'
content_hash: 'sha256:ba69ac639d8a20e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# isPictureInPictureSupported()

<sub>Type Method</sub>

Returns a Boolean value that indicates whether the current device supports Picture in Picture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func isPictureInPictureSupported() -> Bool
```

## Return Value

`true` if the current device supports Picture in Picture playback, otherwise `false`.

## Discussion

If Picture in Picture isn’t supported on the current device, attempting to initialize a Picture in Picture controller returns `nil`.

## See Also

### Accessing Picture in Picture State

- [pictureInPicturePossible](ispictureinpicturepossible.md) — A Boolean value that indicates whether Picture in Picture playback is currently possible.
- [pictureInPictureActive](ispictureinpictureactive.md) — A Boolean value that indicates whether the Picture in Picture window is onscreen.
- [pictureInPictureSuspended](ispictureinpicturesuspended.md) — A Boolean value that indicates whether the system suspends the controller’s Picture in Picture window.
