---
title: 'enqueueImmediately(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueimmediately(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueimmediately(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueueimmediately%28_%3A%29.json'
content_hash: 'sha256:e54744d1e4f8f665'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# enqueueImmediately(_:)

<sub>Instance Method</sub>

Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func enqueueImmediately(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult
```

## Parameters

- `sampleBuffer` — The sample buffer to enqueue.

## Return Value

The result of the enqueue operation.

## See Also

### Enqueuing sample buffers

- [enqueue(_:)](<enqueue(__).md>) — Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [EnqueueResult](enqueueresult.md) — A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.
