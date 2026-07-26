---
title: contentSource
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.property
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.property.json'
content_hash: 'sha256:6fda09075b2503a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# contentSource

<sub>Instance Property</sub>

The source of the controller’s content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var contentSource: AVPictureInPictureController.ContentSource? { get set }
```

## Discussion

You can change a content source while a Picture in Picture session is active, but only if the new content source is ready for display. If it isn’t ready, the session ends immediately.

If your app uses [AVPlayerLayer](../../avfoundation/avplayerlayer.md), verify that the value of its [isReadyForDisplay](../../avfoundation/avplayerlayer/isreadyfordisplay.md) property is `true` before setting it as a content source.

## See Also

### Configuring the Content Source

- [ContentSource](contentsource-swift.class.md) — An object that represents the source of the content to present in Picture in Picture.
