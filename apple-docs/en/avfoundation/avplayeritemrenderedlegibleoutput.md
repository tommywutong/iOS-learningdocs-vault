---
title: AVPlayerItemRenderedLegibleOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemrenderedlegibleoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemrenderedlegibleoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemrenderedlegibleoutput.json'
content_hash: 'sha256:cefda211fa5d70c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemRenderedLegibleOutput

<sub>Class</sub>

A player item output that vends media with a legible characteristic as rendered pixel buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class AVPlayerItemRenderedLegibleOutput
```

## Relationships

- **Inherits From**: [AVPlayerItemOutput](avplayeritemoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating an output

- [- initWithVideoDisplaySize:](<avplayeritemrenderedlegibleoutput/init(videodisplay_).md>) — Creates a rendered legible output object.

### Configuring an output

- [advanceIntervalForDelegateInvocation](avplayeritemrenderedlegibleoutput/advanceintervalfordelegateinvocation.md) — Permits advance invocation of the associated delegate, if any.
- [videoDisplaySize](avplayeritemrenderedlegibleoutput/videodisplaysize.md) — Set the video display size to use for rendering of pixel buffers.

### Setting a delegate

- [delegate](avplayeritemrenderedlegibleoutput/delegate.md) — A delegate object for this output.
- [- setDelegate:queue:](<avplayeritemrenderedlegibleoutput/setdelegate(__queue_).md>) — Sets the delegate object and the queue on which it’s invoked.
- [delegateQueue](avplayeritemrenderedlegibleoutput/delegatequeue.md) — The dispatch queue on which the output calls the delegate object.
- [AVPlayerItemRenderedLegibleOutputPushDelegate](avplayeritemrenderedlegibleoutputpushdelegate.md) — A delegate that handles the rendered pixel buffers produced by a rendered legible output object.

### Initializers

- [init(videoDisplaySize:)](<avplayeritemrenderedlegibleoutput/init(videodisplaysize_).md>)

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVVideoOutputSpecification](avvideooutputspecification.md) — An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [AVPlayerItemOutput](avplayeritemoutput.md) — An abstract class that defines the common interface to output media data from a player item.
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — An object that outputs video frames from a player item.
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md) — An object that vends attributed strings for media with a legible characteristic.
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — An object that provides a rendered pixel buffer and its position in pixels.
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — An object that vends collections of metadata items that a player item’s tracks carry.
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback. _(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
