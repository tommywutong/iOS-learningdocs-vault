---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, tvOS 17.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/error.json'
content_hash: 'sha256:a7d7b0c355b962a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferVideoRenderer](../avsamplebuffervideorenderer.md)

# error

<sub>Instance Property</sub>

An object the describes the error that caused the rendering failure.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

This value is `nil` by default. It only contains a valid error object when the [status](status.md) value is [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md).

## See Also

### Inspecting the status

- [status](status.md) — A status value that indicates whether this object can enqueue and render sample buffers. _(deprecated)_
