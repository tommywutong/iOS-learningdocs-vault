---
title: AVSampleBufferAudioRenderer.Receiver.RenderingEvent
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent.json'
content_hash: 'sha256:c944d753caa15f61'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../avsamplebufferaudiorenderer.md) · [Receiver](../receiver.md)

# AVSampleBufferAudioRenderer.Receiver.RenderingEvent

<sub>Enumeration</sub>

Events that might require intervention after there are no more samples to enqueue, but before rendering has finished.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum RenderingEvent
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Rendering events

- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged](renderingevent/outputconfigurationchanged.md) — Indicates that the audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](<renderingevent/wasflushedautomatically(at_).md>) — The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](<renderingevent/failed(__).md>) — Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.

## See Also

### Observing rendering events

- [renderingEventsAfterFinishedEnqueuing](renderingeventsafterfinishedenqueuing.md) — A sequence of events that may occur when rendering after enqueuing samples has finished.
