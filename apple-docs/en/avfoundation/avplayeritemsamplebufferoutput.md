---
title: AVPlayerItemSampleBufferOutput
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avplayeritemsamplebufferoutput
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritemsamplebufferoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritemsamplebufferoutput.json'
content_hash: 'sha256:7d0f52351f221e4f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerItemSampleBufferOutput

<sub>Class</sub>

[AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) delivers `CMSampleBuffers` for [AVPlayerItem](avplayeritem.md) playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVPlayerItemSampleBufferOutput
```

## Overview

Playback only happens when the [AVPlayerItem](avplayeritem.md) is the current item of its [AVPlayer](avplayer.md).

Create an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) with a [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) to configure it to deliver `CMSampleBuffers` containing the decoded audio, and attach it to the [AVPlayerItem](avplayeritem.md) using `-[AVPlayerItem addOutput:]`; the audio will be in the format specified by the configuration object’s `requestedAudioFormat`.

Note that [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md) may be used to pull `CMSampleBuffers` far ahead of the current play time.  Practical use requires clients to monitor the item timebase time, and pause pulling when they have received CMSampleBuffers sufficient to prepare for near-term-future playback or processing.

Marker-only `CMSampleBuffers` may be among those returned; you can detect and skip these by testing whether `CMSampleBufferGetNumSamples(sampleBuffer) == 0`.

The output `CMSampleBuffers` will have appropriate OutputPresentationTimeStamps for playback, but beyond that, synchronizing presentation to the AVPlayerItem’s timebase is entirely up to the client.

Currently supported for HLS `AVPlayerItems` only, and only for delivering decoded PCM audio.

## Relationships

- **Inherits From**: [AVPlayerItemOutput](avplayeritemoutput.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a sample buffer output

- [- initWithConfiguration:](<avplayeritemsamplebufferoutput/init(configuration_).md>) — Initializes an instance of [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_

### Retrieving sample buffers

- [nextAvailableSampleBuffer()](<avplayeritemsamplebufferoutput/nextavailablesamplebuffer().md>) — Returns the next sample buffer if it is already available.
- [nextSampleBuffer()](<avplayeritemsamplebufferoutput/nextsamplebuffer().md>) — Returns next sample buffer once it becomes available.
- [SampleBufferInSequence](avplayeritemsamplebufferoutput/samplebufferinsequence.md) — Holds the information necessary for processing generated sample buffers.

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
- [AVPlayerItemSampleBufferOutputConfiguration](avplayeritemsamplebufferoutputconfiguration.md) — Configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
- [AVPlayerItemSampleBufferOutputAudioConfiguration](avplayeritemsamplebufferoutputaudioconfiguration.md) — Audio-specific configuration options specified when creating an [AVPlayerItemSampleBufferOutput](avplayeritemsamplebufferoutput.md). _(beta)_
