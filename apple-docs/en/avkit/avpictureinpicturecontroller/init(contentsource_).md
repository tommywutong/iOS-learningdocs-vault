---
title: 'init(contentSource:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontroller/init(contentsource:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/init(contentsource:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/init%28contentsource%3A%29.json'
content_hash: 'sha256:18786d68ae47e992'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# init(contentSource:)

<sub>Initializer</sub>

Creates a Picture in Picture controller with a content source.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(contentSource: AVPictureInPictureController.ContentSource)
```

## Parameters

- `contentSource` — The source of the content to show in a Picture in Picture window.

## Discussion

Use this initializer to create a controller that displays its content in a player layer or a sample buffer display layer.

> [!important] Important
> Before attempting to create a controller, verify that the current device supports Picture in Picture by calling the [+ isPictureInPictureSupported](<ispictureinpicturesupported().md>) class method. Attempting to create a Picture in Picture controller on an unsupported device returns `nil`.

## See Also

### Creating a Controller

- [- initWithPlayerLayer:](<init(playerlayer_).md>) — Creates a Picture in Picture controller with a player layer.
