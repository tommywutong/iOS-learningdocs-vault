---
title: 'pictureInPictureController(_:failedToStartPictureInPictureWithError:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:failedtostartpictureinpicturewitherror:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller%28_%3Afailedtostartpictureinpicturewitherror%3A%29.json'
content_hash: 'sha256:f5b4ef0891050ea2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureControllerDelegate](../avpictureinpicturecontrollerdelegate.md)

# pictureInPictureController(_:failedToStartPictureInPictureWithError:)

<sub>Instance Method</sub>

Tells the delegate that Picture in Picture failed to start.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, failedToStartPictureInPictureWithError error: any Error)
```

## Parameters

- `pictureInPictureController` — The delegating controller.

- `error` — An error that describes the details of the failure.

## See Also

### Responding to Picture in Picture Lifecycle Events

- [- pictureInPictureControllerWillStartPictureInPicture:](<pictureinpicturecontrollerwillstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to start.
- [- pictureInPictureControllerDidStartPictureInPicture:](<pictureinpicturecontrollerdidstartpictureinpicture(__).md>) — Tells the delegate that Picture in Picture started.
- [- pictureInPictureControllerWillStopPictureInPicture:](<pictureinpicturecontrollerwillstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture is about to stop.
- [- pictureInPictureControllerDidStopPictureInPicture:](<pictureinpicturecontrollerdidstoppictureinpicture(__).md>) — Tells the delegate that Picture in Picture stopped.
