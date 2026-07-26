---
title: AVSampleBufferAudioRenderer.Receiver.EnqueueResult
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult.json'
content_hash: 'sha256:44f7466a0e24542c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../avsamplebufferaudiorenderer.md) · [Receiver](../receiver.md)

# AVSampleBufferAudioRenderer.Receiver.EnqueueResult

<sub>Enumeration</sub>

A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum EnqueueResult
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Enqueue results

- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued](enqueueresult/enqueued.md) — The sample buffer was enqueued successfully.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueuedWithSuggestedFlush(_:)](<enqueueresult/enqueuedwithsuggestedflush(__).md>) — The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](enqueueresult/cancelledduetoflush.md) — The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](<enqueueresult/cancelledduetoerror(__).md>) — The sample buffer was not enqueued because the Receiver failed.

## See Also

### Enqueuing sample buffers

- [enqueue(_:)](<enqueue(__).md>) — Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [enqueueImmediately(_:)](<enqueueimmediately(__).md>) — Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
