---
title: 'enqueue(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueue(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueue(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/enqueue%28_%3A%29.json'
content_hash: 'sha256:812b528775aec2fc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# enqueue(_:)

<sub>Instance Method</sub>

Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func enqueue(_ sampleBuffer: CMReadySampleBuffer<CMSampleBuffer.DynamicContent>) async throws -> AVSampleBufferVideoRenderer.Receiver.EnqueueResult
```

## Parameters

- `sampleBuffer` — The sample buffer to enqueue.

## Return Value

The result of the enqueue operation.

## Discussion

> [!danger] Throws
> `CancellationError` if the Task was cancelled.

## See Also

### Enqueuing sample buffers

- [enqueueImmediately(_:)](<enqueueimmediately(__).md>) — Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [EnqueueResult](enqueueresult.md) — A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.
