---
title: 'init(playerLayer:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontroller/init(playerlayer:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/init(playerlayer:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/init%28playerlayer%3A%29.json'
content_hash: 'sha256:bfede4adfabbf497'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# init(playerLayer:)

<sub>Initializer</sub>

Creates a Picture in Picture controller with a player layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(playerLayer: AVPlayerLayer)
```

## Parameters

- `playerLayer` — The player layer from which to source the media content for the Picture in Picture controller.

## Discussion

For Picture in Picture to work correctly, maintain a strong reference to this object whether your app is running in the foreground or background.

> [!important] Important
> Before attempting to create a controller instance, verify that the current device supports Picture in Picture by calling the [+ isPictureInPictureSupported](<ispictureinpicturesupported().md>) class method. Attempting to create a Picture in Picture controller on an unsupported device returns `nil`.

## See Also

### Creating a Controller

- [- initWithContentSource:](<init(contentsource_).md>) — Creates a Picture in Picture controller with a content source.
