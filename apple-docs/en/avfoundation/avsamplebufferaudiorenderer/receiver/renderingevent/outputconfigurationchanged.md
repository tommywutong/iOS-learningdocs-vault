---
title: AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/renderingevent/outputconfigurationchanged.json'
content_hash: 'sha256:fad922332a5b42d2'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../../avsamplebufferaudiorenderer.md) · [Receiver](../../receiver.md) · [RenderingEvent](../renderingevent.md)

# AVSampleBufferAudioRenderer.Receiver.RenderingEvent.outputConfigurationChanged

<sub>Case</sub>

Indicates that the audio output configuration has changed.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case outputConfigurationChanged
```

## See Also

### Rendering events

- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.wasFlushedAutomatically(at:)](<wasflushedautomatically(at_).md>) — The enqueued media data has been flushed for a reason other than a call to the `flush()` method.
- [AVSampleBufferAudioRenderer.Receiver.RenderingEvent.failed(_:)](<failed(__).md>) — Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.
