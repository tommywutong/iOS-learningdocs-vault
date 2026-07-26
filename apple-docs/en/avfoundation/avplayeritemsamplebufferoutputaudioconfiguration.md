---
title: AVPlayerItemSampleBufferOutputAudioConfiguration
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutputaudioconfiguration.json'
content_hash: 'sha256:e52215f02b4b8de7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemSampleBufferOutputAudioConfiguration

<sub>Class</sub>

Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemSampleBufferOutputAudioConfiguration
```

## Relationships

- **Inherits From**: [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Configuring audio output

- [requestedAudioFormat](avplayeritemsamplebufferoutputaudioconfiguration/requestedaudioformat.md) — Indicates the audio format in which the client prefers to receive the output sample buffers. _(beta)_

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVVideoOutputSpecification](avvideooutputspecification.md) — An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [AVPlayerItemOutput](avplayeritemoutput.md) — An abstract class that defines the common interface to output media data from a player item.
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — An object that outputs video frames from a player item.
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md) — An object that vends attributed strings for media with a legible characteristic.
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md) — A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — An object that provides a rendered pixel buffer and its position in pixels.
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — An object that vends collections of metadata items that a player item’s tracks carry.
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback. _(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
