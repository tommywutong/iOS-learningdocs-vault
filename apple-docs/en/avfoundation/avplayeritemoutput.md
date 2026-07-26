---
title: AVPlayerItemOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemoutput.json'
content_hash: 'sha256:ed9c1c9d2ec714f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemOutput

<sub>Class</sub>

An abstract class that defines the common interface to output media data from a player item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemOutput
```

## Overview

This class provides basic methods for converting time values to the timebase of the item. It also provides an option to suppress rendering of the output associated with the specific instance of this class.

> [!important] Important
> Don’t create instances of this class directly but instead use one of the concrete subclasses that manage specific types of assets.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md), [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md), [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md), [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md), [AVPlayerItemVideoOutput](avplayeritemvideooutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Time conversion

- [- itemTimeForHostTime:](<avplayeritemoutput/itemtime(forhosttime_).md>) — Converts a host time, specified in seconds, to the item’s timebase.
- [- itemTimeForMachAbsoluteTime:](<avplayeritemoutput/itemtime(formachabsolutetime_).md>) — Converts a Mach host time to the item’s timebase.
- [- itemTimeForCVTimeStamp:](<avplayeritemoutput/itemtime(for_).md>) — Converts a Core Video timestamp to the item’s timebase.

### Configuring the playback options

- [suppressesPlayerRendering](avplayeritemoutput/suppressesplayerrendering.md) — A Boolean value that indicates whether the player object renders the receiver’s output.

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVVideoOutputSpecification](avvideooutputspecification.md) — An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [AVPlayerItemVideoOutput](avplayeritemvideooutput.md) — An object that outputs video frames from a player item.
- [AVPlayerItemLegibleOutput](avplayeritemlegibleoutput.md) — An object that vends attributed strings for media with a legible characteristic.
- [AVPlayerItemRenderedLegibleOutput](avplayeritemrenderedlegibleoutput.md) — A player item output that vends media with a legible characteristic as rendered pixel buffers.
- [AVRenderedCaptionImage](avrenderedcaptionimage.md) — An object that provides a rendered pixel buffer and its position in pixels.
- [AVPlayerItemMetadataOutput](avplayeritemmetadataoutput.md) — An object that vends collections of metadata items that a player item’s tracks carry.
- [AVPlayerItemOutputPushDelegate](avplayeritemoutputpushdelegate.md) — A protocol that defines the methods to implement to respond to changes in the media data sequence.
- [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) — [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback. _(beta)_
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
