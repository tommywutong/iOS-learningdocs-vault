---
title: flush()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush%28%29.json'
content_hash: 'sha256:25be0f35abcf0c97'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# flush()

<sub>Instance Method</sub>

Instructs the receiver to discard pending enqueued sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flush()
```

## Discussion

Additional sample buffers can be appended after `flush()`.

> [!note] Note
> For video, it is not possible to determine which sample buffers have been decoded, so the next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing the receiver

- [flush(removingDisplayedImage:)](<flush(removingdisplayedimage_).md>) — Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.
