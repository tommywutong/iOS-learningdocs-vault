---
title: renderingEventsAfterFinishedEnqueuing
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingeventsafterfinishedenqueuing.json'
content_hash: 'sha256:869feeaf68f06982'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# renderingEventsAfterFinishedEnqueuing

<sub>Instance Property</sub>

A sequence of events that may occur when rendering after enqueuing samples has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var renderingEventsAfterFinishedEnqueuing: some Sendable & AsyncSequence<AVSampleBufferVideoRenderer.Receiver.RenderingEvent, Never> { get }
```

## Discussion

After enqueuing samples, iterate over this sequence to discover any issues that may occur while the renderer continues rendering. Break out of the iteration when done monitoring rendering events.

## See Also

### Observing rendering events

- [RenderingEvent](renderingevent.md) — Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.
