---
title: AVQueuedSampleBufferRenderingStatus.failed
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 10.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrenderingstatus/failed
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus/failed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrenderingstatus/failed.json'
content_hash: 'sha256:06b1f3923cf072a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRenderingStatus](../avqueuedsamplebufferrenderingstatus.md)

# AVQueuedSampleBufferRenderingStatus.failed

<sub>Case</sub>

The object can no longer render sample buffers because of an error.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case failed
```

## See Also

### Status values

- [AVQueuedSampleBufferRenderingStatusUnknown](unknown.md) — The object doesn’t have any sample buffers enqueued. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatusRendering](rendering.md) — The object is rendering the sample buffer. _(deprecated)_
