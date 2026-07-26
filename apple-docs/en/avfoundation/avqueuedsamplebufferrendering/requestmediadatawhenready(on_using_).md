---
title: 'requestMediaDataWhenReady(on:using:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/requestmediadatawhenready(on:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/requestmediadatawhenready%28on%3Ausing%3A%29.json'
content_hash: 'sha256:678d62d6fddb843e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# requestMediaDataWhenReady(on:using:)

<sub>Instance Method</sub>

Tells the target to invoke a client-supplied block in order to gather sample buffers for playback.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver to enqueue samples on a detached Task instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func requestMediaDataWhenReady(on queue: dispatch_queue_t, using block: @escaping @Sendable () -> Void)
```

## Parameters

- `queue` — The dispatch queue.

- `block` — A block that enqueues sample buffers until the receiver is no longer ready or there is no more data to supply.

## Discussion

When this method is called multiple times, only the last call is implemented. Pair each call to [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) with a corresponding call to [- stopRequestingMediaData](<stoprequestingmediadata().md>). Releasing the `AVQueuedSampleBufferRendering` object without a call to `stopRequestingMediaData` results in undefined behavior.

## See Also

### Requesting media

- [readyForMoreMediaData](isreadyformoremediadata.md) — A Boolean value that indicates whether the receiver is able to accept more sample buffers. _(deprecated)_
- [- enqueueSampleBuffer:](<enqueue(__).md>) — Sends a sample buffer to the queue for rendering. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) call. _(deprecated)_
