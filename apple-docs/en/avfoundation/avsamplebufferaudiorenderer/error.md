---
title: error
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/error
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/error.json'
content_hash: 'sha256:477c2f4c65708a49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVSampleBufferAudioRenderer](../avsamplebufferaudiorenderer.md)

# error

<sub>Instance Property</sub>

The error that caused the renderer to no longer render sample buffers.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var error: (any Error)? { get }
```

## Discussion

The value of this property is nil unless the value of [status](status.md) is [AVQueuedSampleBufferRenderingStatusFailed](../avqueuedsamplebufferrenderingstatus/failed.md).
