---
title: flush()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.8+, tvOS 10.2+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/flush()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/flush()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/flush%28%29.json'
content_hash: 'sha256:6330390de0a629b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# flush()

<sub>Instance Method</sub>

Instructs the layer to discard any enqueued sample buffers that are pending.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flush()
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [- flush](<../avqueuedsamplebufferrendering/flush().md>) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

Because it’s not possible to determine which sample buffers have been decoded, the next frame passed to [- enqueueSampleBuffer:](<enqueue(__).md>) should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing sample buffers

- [- flushAndRemoveImage](<flushandremoveimage().md>) — Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image. _(deprecated)_
