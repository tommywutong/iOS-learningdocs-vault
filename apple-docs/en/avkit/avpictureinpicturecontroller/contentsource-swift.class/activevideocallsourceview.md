---
title: activeVideoCallSourceView
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview.json'
content_hash: 'sha256:a1c93004f684db42'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# activeVideoCallSourceView

<sub>Instance Property</sub>

The view that contains the video content of the call.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var activeVideoCallSourceView: UIView? { get }
```

## Discussion

The controller uses this view’s layout frame and visibility to determine whether or not Picture in Picture begins automatically when the app moves to the background. The view’s layout frame also influences the animation when entering and exiting Picture in Picture.

## See Also

### Accessing the Active Call Presentation

- [activeVideoCallContentViewController](activevideocallcontentviewcontroller.md) — The view controller that presents the video call content.
- [AVPictureInPictureVideoCallViewController](../../avpictureinpicturevideocallviewcontroller.md) — A view controller that presents content from a video call in Picture in Picture.
