---
title: 'append(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinput/append(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/append(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/append%28_%3A%29.json'
content_hash: 'sha256:192cbc3d16b38a34'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# append(_:)

<sub>Instance Method</sub>

Appends a sample buffer to an input to write to the output file.

> [!warning] Deprecated
> Use SampleBufferReceiver.append(_:) instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func append(_ sampleBuffer: CMSampleBuffer) -> Bool
```

## Parameters

- `sampleBuffer` — The sample buffer to append.

## Return Value

[true](../../swift/true.md) if the input successfully appends the sample buffer; otherwise, [false](../../swift/false.md).

## Discussion

Order the samples you append according to storage requirements. For example, if you’re working with sample buffers containing compressed video, order and append them according to their decode timestamp. The system uses the timing information in the sample buffer relative to the time you set in the call to [- startSessionAtSourceTime:](<../avassetwriter/startsession(atsourcetime_).md>) to determine the timing of samples in the output file.

If this method returns [false](../../swift/false.md), check the value of the asset writer’s [status](../avassetwriter/status-swift.property.md) property to determine whether the writing operation’s status is complete, failed, or canceled. If the status is [AVAssetWriterStatusFailed](../avassetwriter/status-swift.enum/failed.md), the asset writer’s [error](../avassetwriter/error.md) property contains an error object that describes the failure.

> [!important] Important
> Don’t modify the sample buffer or its contents after you’ve passed it to this method.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the input to request media data, at its convenience, to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
