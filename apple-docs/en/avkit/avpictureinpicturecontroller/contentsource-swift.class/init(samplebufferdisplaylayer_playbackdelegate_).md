---
title: 'init(sampleBufferDisplayLayer:playbackDelegate:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(samplebufferdisplaylayer:playbackdelegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init%28samplebufferdisplaylayer%3Aplaybackdelegate%3A%29.json'
content_hash: 'sha256:65f97f104d565a08'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# init(sampleBufferDisplayLayer:playbackDelegate:)

<sub>Initializer</sub>

Creates a content source with a sample buffer display layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
init(sampleBufferDisplayLayer: AVSampleBufferDisplayLayer, playbackDelegate: any AVPictureInPictureSampleBufferPlaybackDelegate)
```

## Parameters

- `sampleBufferDisplayLayer` — The sample buffer display layer to show in Picture in Picture.

- `playbackDelegate` — The playback delegate object that responds to Picture in Picture events.

## See Also

### Creating a Content Source

- [- initWithPlayerLayer:](<init(playerlayer_).md>) — Creates a content source with a player layer.
- [- initWithActiveVideoCallSourceView:contentViewController:](<init(activevideocallsourceview_contentviewcontroller_).md>) — Creates a content source with an active video call.
