---
title: AVQueuedSampleBufferRendering
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avqueuedsamplebufferrendering
source_url: 'https://developer.apple.com/documentation/avfoundation/avqueuedsamplebufferrendering'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avqueuedsamplebufferrendering.json'
content_hash: 'sha256:869dabde3811786a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVQueuedSampleBufferRendering

<sub>Protocol</sub>

Methods you can implement to enqueue sample buffers for presentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVQueuedSampleBufferRendering : NSObjectProtocol
```

## Overview

[AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) and [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) conform to this protocol. When used in conjunction with an [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md), an object conforming to `AVQueuedSampleBufferRendering` can only be attached to a single synchronizer.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Conforming Types**: [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md), [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md), [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md)

## Topics

### Requesting media

- [readyForMoreMediaData](avqueuedsamplebufferrendering/isreadyformoremediadata.md) — A Boolean value that indicates whether the receiver is able to accept more sample buffers. _(deprecated)_
- [- enqueueSampleBuffer:](<avqueuedsamplebufferrendering/enqueue(__).md>) — Sends a sample buffer to the queue for rendering. _(deprecated)_
- [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avqueuedsamplebufferrendering/requestmediadatawhenready(on_using_).md>) — Tells the target to invoke a client-supplied block in order to gather sample buffers for playback. _(deprecated)_
- [- stopRequestingMediaData](<avqueuedsamplebufferrendering/stoprequestingmediadata().md>) — Cancels any current [- requestMediaDataWhenReadyOnQueue:usingBlock:](<avqueuedsamplebufferrendering/requestmediadatawhenready(on_using_).md>) call. _(deprecated)_

### Determining playback readiness

- [hasSufficientMediaDataForReliablePlaybackStart](avqueuedsamplebufferrendering/hassufficientmediadataforreliableplaybackstart.md) — A Boolean value that indicates whether the enqued media meets the required preroll level for reliable playback. _(deprecated)_

### Clearing queued sample buffers

- [- flush](<avqueuedsamplebufferrendering/flush().md>) — Discards all pending enqueued sample buffers. _(deprecated)_

### Indentifying the timebase

- [timebase](avqueuedsamplebufferrendering/timebase.md) — The timebase for a renderer.

## See Also

### Presentation

- [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) — An object used to synchronize multiple queued sample buffers to a single timeline.
- [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) — An object that displays compressed or uncompressed video frames.
- [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md) — An object that enqueues video sample buffers for rendering.
- [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) — An object used to decompress audio and play compressed or uncompressed audio.
