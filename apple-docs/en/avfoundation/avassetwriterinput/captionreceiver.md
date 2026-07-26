---
title: AVAssetWriterInput.CaptionReceiver
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/captionreceiver
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/captionreceiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/captionreceiver.json'
content_hash: 'sha256:aa91f93ea46abb71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# AVAssetWriterInput.CaptionReceiver

<sub>Class</sub>

Provides an interface for writing caption data to an input.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class CaptionReceiver
```

## Topics

### Appending captions

- [append(_:)](<captionreceiver/append(__)-4opbd.md>) — Suspends until the input is ready for more media data, then appends the caption group.
- [append(_:)](<captionreceiver/append(__)-4wpi2.md>) — Suspends until the input is ready for more media data, then appends the caption.
- [appendImmediately(_:)](<captionreceiver/appendimmediately(__)-7q21r.md>) — Appends the caption group synchronously if the input is ready for more media data.
- [appendImmediately(_:)](<captionreceiver/appendimmediately(__)-9uy14.md>) — Appends the caption synchronously if the input is ready for more media data.
- [finish()](<captionreceiver/finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

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
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
