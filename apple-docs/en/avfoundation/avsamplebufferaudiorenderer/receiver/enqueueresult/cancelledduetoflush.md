---
title: AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoflush
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoflush'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoflush.json'
content_hash: 'sha256:04f0efb364ae25c9'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../../avsamplebufferaudiorenderer.md) · [Receiver](../../receiver.md) · [EnqueueResult](../enqueueresult.md)

# AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush

<sub>Case</sub>

The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelledDueToFlush
```

## See Also

### Enqueue results

- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued](enqueued.md) — The sample buffer was enqueued successfully.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueuedWithSuggestedFlush(_:)](<enqueuedwithsuggestedflush(__).md>) — The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](<cancelledduetoerror(__).md>) — The sample buffer was not enqueued because the Receiver failed.
