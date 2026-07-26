---
title: AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflush
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflush'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueresult/cancelledduetoflush.json'
content_hash: 'sha256:b5ba5de817887803'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../../avsamplebuffervideorenderer.md) · [Receiver](../../receiver.md) · [EnqueueResult](../enqueueresult.md)

# AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlush

<sub>Case</sub>

The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case cancelledDueToFlush
```

## See Also

### Enqueue results

- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueued](enqueued.md) — The sample buffer was enqueued successfully.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.enqueuedWithDecodeFailures(_:)](<enqueuedwithdecodefailures(__).md>) — The sample buffer was enqueued successfully, but the receiver failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToFlushRequiredToResume(_:)](<cancelledduetoflushrequiredtoresume(__).md>) — The sample buffer was not enqueued because the Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](<cancelledduetoerror(__).md>) — The sample buffer was not enqueued because the Receiver failed.
