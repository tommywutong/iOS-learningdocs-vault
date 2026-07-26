---
title: AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/enqueued
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/enqueued'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/enqueued.json'
content_hash: 'sha256:e0e15190a515ecd5'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../../avsamplebufferaudiorenderer.md) · [Receiver](../../receiver.md) · [EnqueueResult](../enqueueresult.md)

# AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued

<sub>Case</sub>

The sample buffer was enqueued successfully.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case enqueued
```

## See Also

### Enqueue results

- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueuedWithSuggestedFlush(_:)](<enqueuedwithsuggestedflush(__).md>) — The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](cancelledduetoflush.md) — The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)](<cancelledduetoerror(__).md>) — The sample buffer was not enqueued because the Receiver failed.
