---
title: isReadyForMoreMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering/isreadyformoremediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering/isreadyformoremediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering/isreadyformoremediadata.json'
content_hash: 'sha256:4672737d5c49e991'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRendering](../avqueuedsamplebufferrendering.md)

# isReadyForMoreMediaData

<sub>Instance Property</sub>

A Boolean value that indicates whether the receiver is able to accept more sample buffers.

> [!warning] Deprecated
> Attach renderer to a render synchronizer with sampleBufferReceiver(adding:) and use the receiver's enqueue(_:) async method on its own detached Task to suspend until it is ready for more media data instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isReadyForMoreMediaData: Bool { get }
```

## Discussion

An object conforming to `AVQueuedSampleBufferRendering` keeps track of the occupancy levels of its internal queues for the benefit of clients that enqueue sample buffers from non-real-time sources, for example, clients that can supply sample buffers faster than they are consumed, and so need to decide when to hold back. Clients enqueueing sample buffers from non-real-time sources may hold off from generating or obtaining more sample buffers to enqueue when the value of `readyForMoreMediaData` is `NO`. It is safe to call [- enqueueSampleBuffer:](<enqueue(__).md>) when `readyForMoreMediaData` is `NO`, but don’t enqueue sample buffers without bound.

To help with control of the non-real-time supply of sample buffers, clients can call [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) in order to specify a block that the receiver should invoke whenever it’s ready for sample buffers to be appended.

The value of `readyForMoreMediaData` often changes` from `NO` to `YES` asynchronously, as previously supplied sample buffers are decoded and rendered.

This property is not key-value observable.

## See Also

### Requesting media

- [- enqueueSampleBuffer:](<enqueue(__).md>) — Sends a sample buffer to the queue for rendering. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Tells the target to invoke a client-supplied block in order to gather sample buffers for playback. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) call. _(deprecated)_
