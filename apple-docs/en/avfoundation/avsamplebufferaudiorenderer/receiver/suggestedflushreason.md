---
title: AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer/receiver/suggestedflushreason.json'
content_hash: 'sha256:2c5a463fc28c340a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVSampleBufferAudioRenderer](../../avsamplebufferaudiorenderer.md) · [Receiver](../receiver.md)

# AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason

<sub>Enumeration</sub>

Reasons the receiver suggests the client flush and re-enqueue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SuggestedFlushReason
```

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Flush reasons

- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.outputConfigurationChanged](suggestedflushreason/outputconfigurationchanged.md) — The audio output configuration has changed.
- [AVSampleBufferAudioRenderer.Receiver.SuggestedFlushReason.wasFlushedAutomatically(at:)](<suggestedflushreason/wasflushedautomatically(at_).md>) — The enqueued media data has been flushed for a reason other than a call to the `flush()` method.

## See Also

### Flushing the receiver

- [flush()](<flush().md>) — Instructs the receiver to discard pending enqueued sample buffers.
- [flush(fromSourceTime:)](<flush(fromsourcetime_).md>) — Flushes enqueued sample buffers with presentation time stamps later than or equal to the specified time. This method suspends until the flush is completed.
