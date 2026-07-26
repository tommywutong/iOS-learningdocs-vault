---
title: expectsMediaDataInRealTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassetwriterinput/expectsmediadatainrealtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/expectsmediadatainrealtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/expectsmediadatainrealtime.json'
content_hash: 'sha256:2bfa9a7d01607e37'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# expectsMediaDataInRealTime

<sub>Instance Property</sub>

A Boolean value that indicates whether the input tailors its processing for real-time sources.

> [!warning] Deprecated
> Use the input receiver's appendImmediately(...) method instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var expectsMediaDataInRealTime: Bool { get set }
```

## Discussion

Set this value to [true](../../swift/true.md) if your app appends media data to the input from a real-time source, such as an [AVCaptureOutput](../avcaptureoutput.md). Setting a [true](../../swift/true.md) value optimizes the input for real-time usage so it accurately calculates the state of its [readyForMoreMediaData](isreadyformoremediadata.md) property value.

You can’t set this value after writing starts.

> [!important] Important
> To ensure optimal behavior, don’t set the value of this property and [performsMultiPassEncodingIfSupported](performsmultipassencodingifsupported.md) to [true](../../swift/true.md) at the same time.

## See Also

### Appending media samples

- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
