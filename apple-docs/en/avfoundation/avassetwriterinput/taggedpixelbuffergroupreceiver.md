---
title: AVAssetWriterInput.TaggedPixelBufferGroupReceiver
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/taggedpixelbuffergroupreceiver.json'
content_hash: 'sha256:19fbef0039d1039a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# AVAssetWriterInput.TaggedPixelBufferGroupReceiver

<sub>Class</sub>

Provides an interface for writing tagged pixel buffers to an input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
class TaggedPixelBufferGroupReceiver
```

## Topics

### Appending tagged buffers

- [append(_:with:)](<taggedpixelbuffergroupreceiver/append(__with_).md>) — Suspends until the input is ready for more media data, then appends the tagged pixel buffers.
- [appendImmediately(_:with:)](<taggedpixelbuffergroupreceiver/appendimmediately(__with_).md>) — Appends the tagged pixel buffers synchronously if the input is ready for more media data.
- [finish()](<taggedpixelbuffergroupreceiver/finish().md>) — Indicates to the AVAssetWriter that no more buffers will be appended to this receiver.

### Accessing the pixel buffer pool

- [pixelBufferPool](taggedpixelbuffergroupreceiver/pixelbufferpool.md) — A pixel buffer pool that will vend and efficiently recycle pixel buffer objects that can be appended to the receiver.
- [sourcePixelBufferAttributes](taggedpixelbuffergroupreceiver/sourcepixelbufferattributes.md) — The pixel buffer attributes of pixel buffers that will be vended by the receiver’s pixel buffer pool.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
