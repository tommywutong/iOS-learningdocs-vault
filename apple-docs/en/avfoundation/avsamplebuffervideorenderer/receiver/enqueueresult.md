---
title: AVSampleBufferVideoRenderer.Receiver.EnqueueResult
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult.json'
content_hash: 'sha256:5e3eff35102980c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# AVSampleBufferVideoRenderer.Receiver.EnqueueResult

<sub>Enumeration</sub>

A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum EnqueueResult
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enqueue results

- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](enqueueresult/enqueued.md) — The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)](<enqueueresult/enqueuedwithdecodefailures(__).md>) — The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush](enqueueresult/cancelledduetoflush.md) — The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](<enqueueresult/cancelledduetoflushrequiredtoresume(__).md>) — The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](<enqueueresult/cancelledduetoerror(__).md>) — The sample buffer was not enqueued because the Receiver failed.

## See Also

### Enqueuing sample buffers

- [enqueue(_:)](<enqueue(__).md>) — Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [enqueueImmediately(_:)](<enqueueimmediately(__).md>) — Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
