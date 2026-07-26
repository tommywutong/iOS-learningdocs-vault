---
title: isReadyForMoreMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinput/isreadyformoremediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/isreadyformoremediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/isreadyformoremediadata.json'
content_hash: 'sha256:e47c6a43514eb990'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# isReadyForMoreMediaData

<sub>Instance Property</sub>

A Boolean value that indicates whether the input is ready to accept media data.

> [!warning] Deprecated
> Use the input receiver's async append(...) method instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isReadyForMoreMediaData: Bool { get }
```

## Discussion

An asset writer with multiple inputs writes media data in an interleaved manner for efficient playback and storage. To maintain appropriate interleaving, you can only append data to an input when the value of this property is [true](../../swift/true.md).

Apps that write media data from a non-real-time source, such as an instance of [AVAssetReader](../avassetreader.md), wait to generate or retrieve more media data while this property value is [false](../../swift/false.md). To control of the supply of non-real-time media data, use the [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) method to specify a callback for the input to invoke when it’s ready to append more data.

Apps that write media data from a real-time source, such as an instance of [AVCaptureOutput](../avcaptureoutput.md), set the input’s [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) property value to [true](../../swift/true.md) so that the input accurately determines its readiness for more data. When [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) is [true](../../swift/true.md), this property value becomes [false](../../swift/false.md) only when the input can’t process media samples at the current data rate. If this property value becomes [false](../../swift/false.md) for a real-time source, your app may need to reduce the rate at which it appends samples, or drop them altogether.

If the [canPerformMultiplePasses](canperformmultiplepasses.md) value of any of an asset writer’s inputs is [true](../../swift/true.md), the value of this property may start as [false](../../swift/false.md), and remain that way for extended periods.

The value of this property often changes from [false](../../swift/false.md) to [true](../../swift/true.md) asynchronously, as the asset writer processes and writes media samples to the output. It’s possible for this property value to temporarily be [false](../../swift/false.md) for all inputs.

This property is key-value observable. The system doesn’t notify observers on a specific thread.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
