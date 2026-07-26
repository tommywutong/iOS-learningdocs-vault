---
title: markAsFinished()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+, iPadOS 4.1+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avassetwriterinput/markasfinished()
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/markasfinished()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/markasfinished%28%29.json'
content_hash: 'sha256:58b303117b987ee4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# markAsFinished()

<sub>Instance Method</sub>

Marks the input as finished to indicate that you’re done appending samples to it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func markAsFinished()
```

## Discussion

Apps that monitor an input’s [readyForMoreMediaData](isreadyformoremediadata.md) value must call this method when they finish appending to it. This is necessary to prevent other inputs from stalling because they’re waiting on the input’s media data to complete the ideal interleaving pattern.

After calling this method from the serial queue passed to [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>), the input issues no more invocations of the callback it passes to that method.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
