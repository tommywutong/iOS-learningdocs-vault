---
title: 'AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/enqueueresult/cancelledduetoerror%28_%3A%29.json'
content_hash: 'sha256:1b6ac1b4ee3265c9'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../../avsamplebufferaudiorenderer.md) · [Receiver](../../receiver.md) · [EnqueueResult](../enqueueresult.md)

# AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToError(_:)

<sub>Case</sub>

The sample buffer was not enqueued because the Receiver failed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cancelledDueToError(any Error)
```

## See Also

### Enqueue results

- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueued](enqueued.md) — The sample buffer was enqueued successfully.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.enqueuedWithSuggestedFlush(_:)](<enqueuedwithsuggestedflush(__).md>) — The sample buffer was enqueued successfully, but the receiver suggests that the client flush and re-enqueue.
- [AVSampleBufferAudioRenderer.Receiver.EnqueueResult.cancelledDueToFlush](cancelledduetoflush.md) — The sample buffer was not enqueued because the Receiver was flushed while the enqueue was suspended.
