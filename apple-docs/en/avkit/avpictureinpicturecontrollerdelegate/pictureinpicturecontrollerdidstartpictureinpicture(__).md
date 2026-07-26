---
title: 'pictureInPictureControllerDidStartPictureInPicture(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerdidstartpictureinpicture%28_%3A%29.json'
content_hash: 'sha256:1ea5c6046e719854'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureControllerDelegate](../avpictureinpicturecontrollerdelegate.md)

# pictureInPictureControllerDidStartPictureInPicture(_:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureControllerDidStartPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)
```

## Parameters

- `pictureInPictureController` — The delegating controller.

## See Also

### Responding to Picture in Picture Lifecycle Events

- [- pictureInPictureControllerWillStartPictureInPicture:](<pictureinpicturecontrollerwillstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to start.
- [- pictureInPictureController:failedToStartPictureInPictureWithError:](<pictureinpicturecontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture failed to start.
- [- pictureInPictureControllerWillStopPictureInPicture:](<pictureinpicturecontrollerwillstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to stop.
- [- pictureInPictureControllerDidStopPictureInPicture:](<pictureinpicturecontrollerdidstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture stopped.
