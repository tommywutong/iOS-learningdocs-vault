---
title: AVPictureInPictureController.ContentSource
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class.json'
content_hash: 'sha256:4aa7a97686f1faa8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# AVPictureInPictureController.ContentSource

<sub>Class</sub>

An object that represents the source of the content to present in Picture in Picture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class ContentSource
```

## Overview

The system supports displaying content from an [AVPlayerLayer](../../avfoundation/avplayerlayer.md) or [AVSampleBufferDisplayLayer](../../avfoundation/avsamplebufferdisplaylayer.md) in a Picture in Picture window. Use an instance of this class to describe the source of your app’s content.

## Relationships

- **Inherits From**: [NSObject](../../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../../swift/cvararg.md), [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [CustomStringConvertible](../../swift/customstringconvertible.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [NSObjectProtocol](../../objectivec/nsobjectprotocol.md)

## Topics

### Creating a Content Source

- [- initWithPlayerLayer:](<contentsource-swift.class/init(playerlayer_).md>) — Creates a content source with a player layer.
- [- initWithSampleBufferDisplayLayer:playbackDelegate:](<contentsource-swift.class/init(samplebufferdisplaylayer_playbackdelegate_).md>) — Creates a content source with a sample buffer display layer.
- [- initWithActiveVideoCallSourceView:contentViewController:](<contentsource-swift.class/init(activevideocallsourceview_contentviewcontroller_).md>) — Creates a content source with an active video call.

### Accessing the Presentation Layer

- [playerLayer](contentsource-swift.class/playerlayer.md) — The presenting player layer.
- [sampleBufferDisplayLayer](contentsource-swift.class/samplebufferdisplaylayer.md) — The presenting sample buffer display layer.

### Accessing the Active Call Presentation

- [activeVideoCallSourceView](contentsource-swift.class/activevideocallsourceview.md) — The view that contains the video content of the call.
- [activeVideoCallContentViewController](contentsource-swift.class/activevideocallcontentviewcontroller.md) — The view controller that presents the video call content.
- [AVPictureInPictureVideoCallViewController](../avpictureinpicturevideocallviewcontroller.md) — A view controller that presents content from a video call in Picture in Picture.

### Configuring the Delegate

- [sampleBufferPlaybackDelegate](contentsource-swift.class/samplebufferplaybackdelegate.md) — A delegate object that responds to sample buffer playback events.
- [AVPictureInPictureSampleBufferPlaybackDelegate](../avpictureinpicturesamplebufferplaybackdelegate.md) — A protocol for controlling playback from a sample buffer display layer in Picture in Picture.

### Invalidating State

- [- invalidatePlaybackState](<invalidateplaybackstate().md>) — Invalidates the controller’s current playback state and fetches the updated state from the sample buffer playback delegate object.

## See Also

### Configuring the Content Source

- [contentSource](contentsource-swift.property.md) — The source of the controller’s content.
