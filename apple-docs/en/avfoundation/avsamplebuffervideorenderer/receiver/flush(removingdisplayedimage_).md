---
title: 'flush(removingDisplayedImage:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush(removingdisplayedimage:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush(removingdisplayedimage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/flush%28removingdisplayedimage%3A%29.json'
content_hash: 'sha256:ea0a7466c5b6a0cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# flush(removingDisplayedImage:)

<sub>Instance Method</sub>

Instructs the receiver to discard pending enqueued sample buffers and call the provided block when complete. This method suspends until the flush is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
nonisolated(nonsending) func flush(removingDisplayedImage removeDisplayedImage: Bool) async
```

## Parameters

- `removeDisplayedImage` — Set to true to remove any currently displayed image, false to preserve any current image.

## Discussion

A flush resets decoder state. The next frame passed to enqueueSampleBuffer: should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing the receiver

- [flush()](<flush().md>) — Instructs the receiver to discard pending enqueued sample buffers.
