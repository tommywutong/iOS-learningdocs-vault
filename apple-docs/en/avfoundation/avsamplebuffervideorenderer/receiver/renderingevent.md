---
title: AVSampleBufferVideoRenderer.Receiver.RenderingEvent
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent.json'
content_hash: 'sha256:4bb92d1b3f17df62'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../avsamplebuffervideorenderer.md) · [Receiver](../receiver.md)

# AVSampleBufferVideoRenderer.Receiver.RenderingEvent

<sub>Enumeration</sub>

Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum RenderingEvent
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Rendering events

- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)](<renderingevent/didfailtodecode(__).md>) — Indicates that the renderer failed to decode one or more previously enqueued sample buffers.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)](<renderingevent/requiresflushtoresumedecoding(__).md>) — The Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)](<renderingevent/failed(__).md>) — Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

## See Also

### Observing rendering events

- [renderingEventsAfterFinishedEnqueuing](renderingeventsafterfinishedenqueuing.md) — A sequence of events that may occur when rendering after enqueuing samples has finished.
