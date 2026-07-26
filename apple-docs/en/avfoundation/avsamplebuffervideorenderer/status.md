---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/status
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/status'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/status.json'
content_hash: 'sha256:63ae2a1f9180ecba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# status

<sub>Instance Property</sub>

A status value that indicates whether this object can enqueue and render sample buffers.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVQueuedSampleBufferRenderingStatus { get }
```

## Discussion

If the status is [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md), check the value of the [error](error.md) property to determine the failure. To resume rendering sample buffers after a failure, you must first reset the status to [AVQueuedSampleBufferRenderingStatusUnknown](../avqueuedsamplebufferrenderingstatus/unknown.md), which you do by invoking [- flush](<../avqueuedsamplebufferrendering/flush().md>) on the video renderer.

This property is key-value observable.

## See Also

### Inspecting the status

- [error](error.md) — An object the describes the error that caused the rendering failure. _(deprecated)_
