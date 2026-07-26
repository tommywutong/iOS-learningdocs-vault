---
title: CMTagCollectionCreateWithVideoOutputPreset
framework: AVFoundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.2+, iPadOS 17.2+, Mac Catalyst 17.2+, macOS 14.2+, tvOS 17.2+, visionOS 1.1+, watchOS 10.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/cmtagcollectioncreatewithvideooutputpreset
source_url: 'https://developer.apple.com/documentation/avfoundation/cmtagcollectioncreatewithvideooutputpreset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/cmtagcollectioncreatewithvideooutputpreset.json'
content_hash: 'sha256:dc0d83f4cf0e8d8e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# CMTagCollectionCreateWithVideoOutputPreset

<sub>Function</sub>

Creates a collection with the required tags to describe the specified video output requirements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern OSStatus CMTagCollectionCreateWithVideoOutputPreset(CFAllocatorRef allocator, CMTagCollectionVideoOutputPreset preset, CMTagCollectionRef*newCollectionOut);
```

## Parameters

- `allocator` — An allocator to use to create the collection and internal data structures.

- `preset` — A preset that indicates the desired output type.

- `newCollectionOut` — The address of the newly created tag collection.

## See Also

### Media output

- [AVPlayerVideoOutput](avplayervideooutput.md) — An object that receives video data from a player object.
- [AVVideoOutputSpecification](avvideooutputspecification.md) — An object that specifies the pixel buffer attributes and tag collections handled by a player video output.
- [CMTagCollectionVideoOutputPreset](cmtagcollectionvideooutputpreset.md) — Constants that indicate the type of video content to output.
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
- [AVPlayerItemSampleBufferOutputDelegate](avplayeritemsamplebufferoutputdelegate.md) — Defines common delegate methods for objects participating in sample buffer output. _(beta)_
