---
title: AVAssetWriterInput.MetadataReceiver
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/metadatareceiver
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/metadatareceiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/metadatareceiver.json'
content_hash: 'sha256:fcfda025a45c9904'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# AVAssetWriterInput.MetadataReceiver

<sub>Class</sub>

Provides an interface for writing timed metadata groups to an input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MetadataReceiver
```

## Topics

### Appending metadata

- [append(_:)](<metadatareceiver/append(__).md>) — Suspends until the input is ready for more media data, then appends the timed metadata group.
- [appendImmediately(_:)](<metadatareceiver/appendimmediately(__).md>) — Appends the timed metadata group synchronously if the input is ready for more media data.
- [finish()](<metadatareceiver/finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
