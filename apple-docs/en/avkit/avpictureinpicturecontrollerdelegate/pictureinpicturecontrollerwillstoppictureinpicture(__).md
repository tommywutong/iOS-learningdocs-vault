---
title: 'pictureInPictureControllerWillStopPictureInPicture(_:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontrollerwillstoppictureinpicture%28_%3A%29.json'
content_hash: 'sha256:16d1b74db36a2f4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureControllerDelegate](../avpictureinpicturecontrollerdelegate.md)

# pictureInPictureControllerWillStopPictureInPicture(_:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture is about to stop.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureControllerWillStopPictureInPicture(_ pictureInPictureController: AVPictureInPictureController)
```

## Parameters

- `pictureInPictureController` — The delegating controller.

## See Also

### Responding to Picture in Picture Lifecycle Events

- [- pictureInPictureControllerWillStartPictureInPicture:](<pictureinpicturecontrollerwillstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to start.
- [- pictureInPictureControllerDidStartPictureInPicture:](<pictureinpicturecontrollerdidstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture started.
- [- pictureInPictureController:failedToStartPictureInPictureWithError:](<pictureinpicturecontroller(__failedtostartpictureinpicturewitherror_).md>) — Tells the delegate that Picture in Picture failed to start.
- [- pictureInPictureControllerDidStopPictureInPicture:](<pictureinpicturecontrollerdidstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture stopped.
