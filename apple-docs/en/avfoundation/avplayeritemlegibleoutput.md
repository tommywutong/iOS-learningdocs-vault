---
title: AVPlayerItemLegibleOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemlegibleoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemlegibleoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemlegibleoutput.json'
content_hash: 'sha256:80938c157120e991'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemLegibleOutput

<sub>Class</sub>

An object that vends attributed strings for media with a legible characteristic.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVPlayerItemLegibleOutput
```

## Relationships

- **Inherits From**: [AVPlayerItemOutput](avplayeritemoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a legible output

- [- initWithMediaSubtypesForNativeRepresentation:](<avplayeritemlegibleoutput/init(mediasubtypesfornativerepresentation_).md>) — Creates an initialized legible-output object.

### Configuring text styling

- [textStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.property.md) — A string identifier indicating the degree of text styling to be applied to attributed strings vended by the  object.
- [TextStylingResolution](avplayeritemlegibleoutput/textstylingresolution-swift.struct.md) — A text styling resolution.

### Configuring the delegate

- [delegate](avplayeritemlegibleoutput/delegate.md) — The delegate of the output class.
- [- setDelegate:queue:](<avplayeritemlegibleoutput/setdelegate(__queue_).md>) — Sets the receiver’s delegate and a dispatch queue on which the delegate is called.
- [AVPlayerItemLegibleOutputPushDelegate](avplayeritemlegibleoutputpushdelegate.md) — Methods you can implement to provide alternative attributed-string output.
- [advanceIntervalForDelegateInvocation](avplayeritemlegibleoutput/advanceintervalfordelegateinvocation.md) — The time interval, in seconds, that a player item legible output object messages its delegate earlier than normal.
- [delegateQueue](avplayeritemlegibleoutput/delegatequeue.md) — The dispatch queue on which the delegate is called.

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVVideoOutputSpecification](avvideooutputspecification.md) — An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [AVPlayerItemOutput](avplayeritemoutput.md) — An abstract class that defines the common interface to output media data from a player item.
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — An object that outputs video frames from a player item.
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md) — A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — An object that provides a rendered pixel buffer and its position in pixels.
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — An object that vends collections of metadata items that a player item’s tracks carry.
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback. _(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
