---
title: activeVideoCallContentViewController
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller.json'
content_hash: 'sha256:15fe881b3fe39b04'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# activeVideoCallContentViewController

<sub>Instance Property</sub>

The view controller that presents the video call content.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var activeVideoCallContentViewController: AVPictureInPictureVideoCallViewController { get }
```

## Discussion

This view controller may indicate a preferred content size which influences the aspect ratio and the size of the Picture in Picture window. The view it presents isn’t interactive and doesn’t receive touches or user input.

When this view controller’s appearance methods indicate that its view is on screen, place the video call content view in the controller’s view hierarchy. The content must fill the bounds of the view controller’s view.

Although apps can choose to move content from their source view to this view controller, it’s also valid to show different views, as long as they represent the same video call.

## See Also

### Accessing the Active Call Presentation

- [activeVideoCallSourceView](activevideocallsourceview.md) — The view that contains the video content of the call.
- [AVPictureInPictureVideoCallViewController](../../avpictureinpicturevideocallviewcontroller.md) — A view controller that presents content from a video call in Picture in Picture.
