---
title: AVVideoOutputSpecification
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideooutputspecification
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideooutputspecification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideooutputspecification.json'
content_hash: 'sha256:c7b5d4a4a7a08bdd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoOutputSpecification

<sub>Class</sub>

An object that specifies the pixel buffer attributes and tag collections handled by a player video output.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVVideoOutputSpecification
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Creating a specification

- [init(tagCollections:)](<avvideooutputspecification/init(tagcollections_).md>)

### Configuring the specification

- [defaultOutputSettings](avvideooutputspecification/defaultoutputsettings.md)
- [setOutputSettings(_:for:)](<avvideooutputspecification/setoutputsettings(__for_).md>)
- [defaultPixelBufferAttributes](avvideooutputspecification/defaultpixelbufferattributes.md) _(deprecated)_
- [setOutputPixelBufferAttributes(_:for:)](<avvideooutputspecification/setoutputpixelbufferattributes(__for_).md>) _(deprecated)_
- [preferredTagCollections](avvideooutputspecification/preferredtagcollections-3gdo7.md)

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVPlayerItemOutput](avplayeritemoutput.md) — An abstract class that defines the common interface to output media data from a player item.
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — An object that outputs video frames from a player item.
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md) — An object that vends attributed strings for media with a legible characteristic.
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md) — A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — An object that provides a rendered pixel buffer and its position in pixels.
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — An object that vends collections of metadata items that a player item’s tracks carry.
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback. _(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
