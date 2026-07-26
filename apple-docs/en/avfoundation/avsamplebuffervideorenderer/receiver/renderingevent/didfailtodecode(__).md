---
title: 'AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)'
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer/receiver/renderingevent/didfailtodecode%28_%3A%29.json'
content_hash: 'sha256:f7fc89f58f1d3ef0'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVSampleBufferVideoRenderer](../../../avsamplebuffervideorenderer.md) · [Receiver](../../receiver.md) · [RenderingEvent](../renderingevent.md)

# AVSampleBufferVideoRenderer.Receiver.RenderingEvent.didFailToDecode(_:)

<sub>Case</sub>

Indicates that the renderer failed to decode one or more previously enqueued sample buffers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case didFailToDecode([any Error])
```

## See Also

### Rendering events

- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.requiresFlushToResumeDecoding(_:)](<requiresflushtoresumedecoding(__).md>) — The Receiver requires a flush to continue enqueuing samples.
- [AVSampleBufferVideoRenderer.Receiver.RenderingEvent.failed(_:)](<failed(__).md>) — Indicates that the receiver cannot currently enqueue or render sample buffers because of the associated error.
