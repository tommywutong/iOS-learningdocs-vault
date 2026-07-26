---
title: 'requestMediaDataWhenReady(on:using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/requestmediadatawhenready(on:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/requestmediadatawhenready%28on%3Ausing%3A%29.json'
content_hash: 'sha256:456dff637c5f8826'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# requestMediaDataWhenReady(on:using:)

<sub>Instance Method</sub>

Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

## Parameters

- `queue` — The dispatch queue.

- `block` — The block that provides media data.

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [- requestMediaDataWhenReadyOnQueue:usingBlock:](<../avqueuedsamplebufferrendering/requestmediadatawhenready(on_using_).md>) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

The block is expected to call the [- enqueueSampleBuffer:](<enqueue(__).md>) in order to provide media data for decompression (if necessary) and rendering while the [readyForMoreMediaData](isreadyformoremediadata.md) property remains [true](../../swift/true.md), or until it can provide no additional media. When the layer has decoded enough media data that it is ready for additional media data, it will invoke the block again.

By allowing the display layer to determine when to invoke the block, the implementation of incremental I/O operations is simplified when supplying synchronized media data during rendering.

If this function is called multiple times, only the last call is effective.

You invoke the [- stopRequestingMediaData](<stoprequestingmediadata().md>) method to cancel this request.

Each call to `requestMediaDataWhenReadyOnQueue:usingBlock:` must be balanced with a corresponding call to [- stopRequestingMediaData](<stoprequestingmediadata().md>).

Releasing the receiver instance without a call to [- stopRequestingMediaData](<stoprequestingmediadata().md>) will result in undefined behavior.

## See Also

### Initiating media data requests

- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates the readiness of the layer to accept more sample buffers. _(deprecated)_
- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current media data request.
- [hasSufficientMediaDataForReliablePlaybackStart](hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level. _(deprecated)_
