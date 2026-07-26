---
title: flush()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering/flush()
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/flush()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/flush%28%29.json'
content_hash: 'sha256:d104aa534806c9b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# flush()

<sub>Instance Method</sub>

Discards all pending enqueued sample buffers.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's flush() method instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func flush()
```

## Discussion

It is not possible to determine which sample buffers have been decoded for video. The next frame passed to [- enqueueSampleBuffer:](<enqueue(__).md>) should be an IDR frame (also known as a key frame or sync sample).
