---
title: AVQueuedSampleBufferRenderingStatus.unknown
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 10.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrenderingstatus/unknown
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus/unknown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrenderingstatus/unknown.json'
content_hash: 'sha256:c28ac909c19bd203'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVQueuedSampleBufferRenderingStatus](../avqueuedsamplebufferrenderingstatus.md)

# AVQueuedSampleBufferRenderingStatus.unknown

<sub>Case</sub>

The object doesn’t have any sample buffers enqueued.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case unknown
```

## See Also

### Status values

- [AVQueuedSampleBufferRenderingStatusRendering](rendering.md) — The object is rendering the sample buffer. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatusFailed](failed.md) — The object can no longer render sample buffers because of an error. _(deprecated)_
