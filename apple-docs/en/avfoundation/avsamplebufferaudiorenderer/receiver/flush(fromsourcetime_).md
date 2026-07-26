---
title: 'flush(fromSourceTime:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush(fromsourcetime:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/flush%28fromsourcetime%3A%29.json'
content_hash: 'sha256:2fb6e4e50baa9f1f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../avsamplebufferaudiorenderer.md) · [Receiver](../receiver.md)

# flush(fromSourceTime:)

<sub>Instance Method</sub>

Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated(nonsending) func flush(fromSourceTime sourceTime: CMTime) async -> Bool
```

## Parameters

- `sourceTime` — The source time for the flush to take effect.

## Return Value

If the flush was successful, this method returns `true`. Otherwise it returns `false`.

## Discussion

This method can be used to replace media data scheduled to be rendered in the future, without interrupting playback.  One example of this is when the data that has already been enqueued is from a sequence of two songs and the second song is swapped for a new song.  In this case, this method would be called with the time stamp of the first sample buffer from the second song.  After this method resumes returning `true`, media data may again be enqueued with timestamps at the specified time.

If this method returns `false`, the flush did not succeed and the set of enqueued sample buffers remains unchanged.  A flush can fail because the source time was too close to (or earlier than) the current time or because the current configuration of the receiver does not support flushing at a particular time.  In these cases, the caller can choose to flush all enqueued media data by invoking the `flush()` method.

## See Also

### Flushing the receiver

- [flush()](<flush().md>) — Instructs the receiver to discard pending enqueued sample buffers.
- [SuggestedFlushReason](suggestedflushreason.md) — Reasons the receiver suggests the client flush and re-enqueue.
