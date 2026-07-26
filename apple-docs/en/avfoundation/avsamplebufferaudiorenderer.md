---
title: AVSampleBufferAudioRenderer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferaudiorenderer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferaudiorenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferaudiorenderer.json'
content_hash: 'sha256:5208126d7d36d174'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferAudioRenderer

<sub>Class</sub>

An object used to decompress audio and play compressed or uncompressed audio.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSampleBufferAudioRenderer
```

## Overview

You must add an instance of this class to an [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) before queuing the first sample buffer.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Determining rendering status

- [status](avsamplebufferaudiorenderer/status.md) — The status of the audio renderer. _(deprecated)_
- [AVQueuedSampleBufferRenderingStatus](avqueuedsamplebufferrenderingstatus.md) — The statuses for sample buffer rendering. _(deprecated)_

### Removing queued buffers

- [- flushFromSourceTime:completionHandler:](<avsamplebufferaudiorenderer/flush(fromsourcetime_completionhandler_).md>) — Flushes queued sample buffers with presentation time stamps later than or equal to the specified time. _(deprecated)_
- [AVSampleBufferAudioRendererFlushTimeKey](avsamplebufferaudiorendererflushtimekey.md) — The key that indicates the presentation timestamp of the first queued sample that was flushed. _(deprecated)_

### Configuring time and pitch

- [audioTimePitchAlgorithm](avsamplebufferaudiorenderer/audiotimepitchalgorithm.md) — The processing algorithm used to manage audio pitch at different rates.
- [AVAudioTimePitchAlgorithm](avaudiotimepitchalgorithm.md) — An algorithm used to set the audio pitch as the rate changes.

### Configuring audio spatialization

- [allowedAudioSpatializationFormats](avsamplebufferaudiorenderer/allowedaudiospatializationformats.md) — The source audio channel layouts the audio renderer supports for spatialization.

### Managing audio output

- [volume](avsamplebufferaudiorenderer/volume.md) — The current audio volume for the audio renderer.
- [muted](avsamplebufferaudiorenderer/ismuted.md) — A Boolean value that indicates whether audio for the renderer is in a muted state.
- [audioOutputDeviceUniqueID](avsamplebufferaudiorenderer/audiooutputdeviceuniqueid.md) — The unique identifier of the output device used to play audio.

### Responding to errors

- [error](avsamplebufferaudiorenderer/error.md) — The error that caused the renderer to no longer render sample buffers. _(deprecated)_

### Classes

- [Receiver](avsamplebufferaudiorenderer/receiver.md)

## See Also

### Presentation

- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) — Methods you can implement to enqueue sample buffers for presentation.
- [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) — An object used to synchronize multiple queued sample buffers to a single timeline.
- [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) — An object that displays compressed or uncompressed video frames.
- [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md) — An object that enqueues video sample buffers for rendering.
