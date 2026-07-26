---
title: AVSampleBufferVideoRenderer.Receiver
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver.json'
content_hash: 'sha256:7019d59fec819ebc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# AVSampleBufferVideoRenderer.Receiver

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class Receiver
```

## Topics

### Enqueuing sample buffers

- [enqueue(_:)](<receiver/enqueue(__).md>) — Suspends until the receiver is ready for more media data, then enqueues a sample buffer in order to render its contents.
- [enqueueImmediately(_:)](<receiver/enqueueimmediately(__).md>) — Enqueues a sample buffer in order to render its contents, without waiting for the renderer to become ready for more media data.
- [EnqueueResult](receiver/enqueueresult.md) — A value indicating the result of a call to `enqueue(_:)` or `enqueueImmediately(_:)`.

### Flushing the receiver

- [flush()](<receiver/flush().md>) — Instructs the receiver to discard pending enqueued sample buffers.
- [flush(removingDisplayedImage:)](<receiver/flush(removingdisplayedimage_).md>) — Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.

### Observing rendering events

- [renderingEventsAfterFinishedEnqueuing](receiver/renderingeventsafterfinishedenqueuing.md) — A sequence of events that may occur when rendering after enqueuing samples has finished.
- [RenderingEvent](receiver/renderingevent.md) — Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.
