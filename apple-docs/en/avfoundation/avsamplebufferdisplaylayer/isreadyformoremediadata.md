---
title: isReadyForMoreMediaData
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（18.0 起废弃）, iPadOS 8.0+（18.0 起废弃）, Mac Catalyst 13.1+（18.0 起废弃）, macOS 10.8+（15.0 起废弃）, tvOS 10.2+（18.0 起废弃）, visionOS 1.0+（2.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferdisplaylayer/isreadyformoremediadata
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferdisplaylayer/isreadyformoremediadata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferdisplaylayer/isreadyformoremediadata.json'
content_hash: 'sha256:171910176d347a2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferDisplayLayer](../avsamplebufferdisplaylayer.md)

# isReadyForMoreMediaData

<sub>Instance Property</sub>

A Boolean value that indicates the readiness of the layer to accept more sample buffers.

> [!warning] Deprecated
> Use sampleBufferRenderer's readyForMoreMediaData instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isReadyForMoreMediaData: Bool { get }
```

## Discussion

Apple discourages the use of this symbol in iOS 17, tvOS 17, and macOS 14 and later. Use [readyForMoreMediaData](../avqueuedsamplebufferrendering/isreadyformoremediadata.md) on the [sampleBufferRenderer](samplebufferrenderer.md) instead.

`AVSampleBufferDisplayLayer` keeps track of the occupancy levels of its internal queues for the benefit of clients that enqueue sample buffers from non-real-time sources — that is, clients that can supply sample buffers faster than they are consumed and need to decide when to hold back buffers.

Clients enqueueing sample buffers from non-real-time sources may hold off from generating or obtaining more sample buffers to enqueue when the value of `readyForMoreMediaData` is [false](../../swift/false.md).

It is safe to call [- enqueueSampleBuffer:](<enqueue(__).md>) when [readyForMoreMediaData](isreadyformoremediadata.md) is [false](../../swift/false.md), but enqueing more sample buffers than are required for timely rendering by the receiver is highly discouraged.

To help with control of the non-real-time supply of sample buffers, such clients should use [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) in order to specify a block that the layer should invoke whenever it’s ready for sample buffers to be appended.

The value of `readyForMoreMediaData` will often change from [false](../../swift/false.md) to [true](../../swift/true.md) asynchronously, as previously supplied sample buffers are decoded and displayed.

> [!important] Important
> This property does not support key-value observing.

## See Also

### Initiating media data requests

- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<requestmediadatawhenready(on_using_).md>) — Instructs the target to invoke a client-supplied block repeatedly, at its convenience, in order to gather sample buffers for display.
- [requiresFlushToResumeDecoding](requiresflushtoresumedecoding.md) — A Boolean value that indicates whether the layer needs to flush its state to continue decoding frames. _(deprecated)_
- [- stopRequestingMediaData](<stoprequestingmediadata().md>) — Cancels any current media data request.
- [hasSufficientMediaDataForReliablePlaybackStart](hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqueued media data meets the renderer’s preroll level. _(deprecated)_
