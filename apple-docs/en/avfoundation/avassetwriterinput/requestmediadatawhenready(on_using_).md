---
title: 'requestMediaDataWhenReady(on:using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.1+（27.0 起废弃）, iPadOS 4.1+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avassetwriterinput/requestmediadatawhenready(on:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avassetwriterinput/requestmediadatawhenready(on:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassetwriterinput/requestmediadatawhenready%28on%3Ausing%3A%29.json'
content_hash: 'sha256:8f235e57dfb06dac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetWriterInput](../avassetwriterinput.md)

# requestMediaDataWhenReady(on:using:)

<sub>Instance Method</sub>

Tells the input to request media data, at its convenience, to write to the output file.

> [!warning] Deprecated
> Use the input receiver's async append(...) method on its own task instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

## Parameters

- `queue` — The queue on which the system invokes the callback.

- `block` — A callback that the input invokes to retrieve additional media data.

## Discussion

Use this method when working with pull-style buffer sources, such as an [AVAssetReaderOutput](../avassetreaderoutput.md). The callback you provide appends media data to the input until its [readyForMoreMediaData](isreadyformoremediadata.md) property becomes [false](../../swift/false.md), or when there’s no more media data to process (at which point you may mark the input as finished by calling its [- markAsFinished](<markasfinished().md>) method). If you don’t mark the input as finished, after the input processes the media data and becomes ready for more, it invokes the callback again to append more data. The example below shows a typical callback implementation.

```swift
let serialQueue = DispatchQueue(label: "RequestMedia")
assetWriterInput?.requestMediaDataWhenReady(on: serialQueue) { [weak self] in
    guard let self = self,
          let assetWriterInput = self.assetWriterInput else { return }
    while self.assetWriterInput!.isReadyForMoreMediaData {
        // Copy the next sample buffer from your source media.
        guard let nextSampleBuffer = copyNextSampleBufferToWrite() else {
            // Mark the input as finished.
            self.assetWriterInput!.markAsFinished()
            break
        }
        // Append the sample buffer to the input.
        self.assetWriterInput!.append(nextSampleBuffer)
    }      
}
```

When working with push-style sources, such as an [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) or [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md), append buffers directly to the asset writer input when you receive them using its [- appendSampleBuffer:](<append(__).md>) method. Using this method helps avoid having to queue up buffers in between the buffer source and the asset writer input.

## See Also

### Appending media samples

- [expectsMediaDataInRealTime](expectsmediadatainrealtime.md) — A Boolean value that indicates whether the input tailors its processing for real-time sources. _(deprecated)_
- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the input is ready to accept media data. _(deprecated)_
- [- appendSampleBuffer:](<append(__).md>) — Appends a sample buffer to an input to write to the output file. _(deprecated)_
- [- markAsFinished](<markasfinished().md>) — Marks the input as finished to indicate that you’re done appending samples to it.
- [SampleBufferReceiver](samplebufferreceiver.md) — Provides an interface for writing sample buffers to an input.
- [PixelBufferReceiver](pixelbufferreceiver.md) — Provides an interface for writing pixel buffers to an input.
- [TaggedPixelBufferGroupReceiver](taggedpixelbuffergroupreceiver.md) — Provides an interface for writing tagged pixel buffers to an input.
- [MetadataReceiver](metadatareceiver.md) — Provides an interface for writing timed metadata groups to an input.
- [CaptionReceiver](captionreceiver.md) — Provides an interface for writing caption data to an input.
