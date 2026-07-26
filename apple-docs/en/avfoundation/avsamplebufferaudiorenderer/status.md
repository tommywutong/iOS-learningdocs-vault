---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/status
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/status.json'
content_hash: 'sha256:dab3483b5f440913'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# status

<sub>Instance Property</sub>

The status of the audio renderer.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

## Discussion

A renderer begins with a status of [AVQueuedSampleBufferRenderingStatusUnknown](../avqueuedsamplebufferrenderingstatus/unknown.md). As you add sample buffers to the queue for rendering, the renderer transitions to either [AVQueuedSampleBufferRenderingStatusRendering](../avqueuedsamplebufferrenderingstatus/rendering.md) or [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md).

If the status is `AVQueuedSampleBufferRenderingStatus.failed`, check the value of the renderer’s error property for information on the error encountered. This property is key value observable.

## See Also

### Determining rendering status

- [AVQueuedSampleBufferRenderingStatus](../avqueuedsamplebufferrenderingstatus.md) — The statuses for sample buffer rendering. _(deprecated)_
