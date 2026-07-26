---
title: AVQueuedSampleBufferRenderingStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+（27.0 起废弃）, iPadOS 8.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.10+（27.0 起废弃）, tvOS 10.2+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 1.0+（27.0 起废弃）]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avqueuedsamplebufferrenderingstatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrenderingstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrenderingstatus.json'
content_hash: 'sha256:7352722de3e035d8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVQueuedSampleBufferRenderingStatus

<sub>Enumeration</sub>

The statuses for sample buffer rendering.

> [!warning] Deprecated
> Use EnqueueResult from enqueue(_:) and enqueueImmediately(_:), and RenderingEvent from renderingEventsAfterFinishedEnqueuing instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVQueuedSampleBufferRenderingStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVQueuedSampleBufferRenderingStatusUnknown](avqueuedsamplebufferrenderingstatus/unknown.md) — The object doesn’t have any sample buffers enqueued. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatusRendering](avqueuedsamplebufferrenderingstatus/rendering.md) — The object is rendering the sample buffer. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatusFailed](avqueuedsamplebufferrenderingstatus/failed.md) — The object can no longer render sample buffers because of an error. _(deprecated)_

### Initializers

- [init(rawValue:)](<avqueuedsamplebufferrenderingstatus/init(rawvalue_).md>) _(deprecated)_

## See Also

### Determining rendering status

- [status](avsamplebufferaudiorenderer/status.md) — The status of the audio renderer. _(deprecated)_
