---
title: flushAndRemoveImage()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.8+（15.0 起废弃）, tvOS 10.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/flushandremoveimage()
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/flushandremoveimage()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/flushandremoveimage%28%29.json'
content_hash: 'sha256:f29e61258536cba9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# flushAndRemoveImage()

<sub>Instance Method</sub>

Instructs the layer to discard pending enqueued sample buffers and remove any currently displayed image.

> [!warning] Deprecated
> Use sampleBufferRenderer's flushWithRemovalOfDisplayedImage:completionHandler: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func flushAndRemoveImage()
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [- flushWithRemovalOfDisplayedImage:completionHandler:](<../avsamplebuffervideorenderer/flush(removingdisplayedimage_completionhandler_).md>) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

It is not possible to determine which sample buffers have been decoded, so the next frame passed to [- enqueueSampleBuffer:](<enqueue(__).md>) should be an IDR frame (also known as a key frame or sync sample).

## See Also

### Flushing sample buffers

- [- flush](<flush().md>) — Instructs the layer to discard any enqueued sample buffers that are pending.
