---
title: AVSampleBufferVideoRenderer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebuffervideorenderer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebuffervideorenderer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebuffervideorenderer.json'
content_hash: 'sha256:4d2dec58ad3fcc60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferVideoRenderer

<sub>Class</sub>

An object that enqueues video sample buffers for rendering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVSampleBufferVideoRenderer
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md), [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Flushing the renderer

- [requiresFlushToResumeDecoding](avsamplebuffervideorenderer/requiresflushtoresumedecoding.md) — A Boolean value that Indicates whether the renderer requires flushing to continue decoding frames. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotification](avsamplebuffervideorenderer/requiresflushtoresumedecodingdidchangenotification.md) — A notification that indicates that the video renderer requires flushing to continue rendering sample buffers. _(deprecated)_
- [AVSampleBufferVideoRendererRequiresFlushToResumeDecodingDidChangeNotificationRequiresFlushKey](avsamplebuffervideorendererrequiresflushtoresumedecodingdidchangenotificationrequiresflushkey.md) _(deprecated)_
- [- flushWithRemovalOfDisplayedImage:completionHandler:](<avsamplebuffervideorenderer/flush(removingdisplayedimage_completionhandler_).md>) — Tells the video renderer to discard pending enqueued sample buffers. _(deprecated)_

### Setting presentation time expectations

- [presentationTimeExpectation](avsamplebuffervideorenderer/presentationtimeexpectation-swift.property.md)
- [PresentationTimeExpectation](avsamplebuffervideorenderer/presentationtimeexpectation-swift.enum.md) — Options that specify the expected presentation time stamps of enqueue samples.

### Inspecting the status

- [status](avsamplebuffervideorenderer/status.md) — A status value that indicates whether this object can enqueue and render sample buffers. _(deprecated)_
- [error](avsamplebuffervideorenderer/error.md) — An object the describes the error that caused the rendering failure. _(deprecated)_

### Accessing the pixel buffer

- [- copyDisplayedPixelBuffer](<avsamplebuffervideorenderer/displayedpixelbuffer().md>)
- [recommendedPixelBufferAttributes](avsamplebuffervideorenderer/recommendedpixelbufferattributes-6zrqb.md) — Recommended pixel buffer attributes for optimal performance when using CMSampleBuffers containing CVPixelbuffers.

### Handling decode failures

- [AVSampleBufferVideoRendererDidFailToDecodeNotification](avsamplebuffervideorenderer/didfailtodecodenotification.md) — A notification that indicates the video renderer fails to decode a sample buffer. _(deprecated)_
- [AVSampleBufferVideoRendererDidFailToDecodeNotificationErrorKey](avsamplebuffervideorenderer/didfailtodecodenotificationerrorkey.md) — A key to retrieve an error object that provides the details of the failure. _(deprecated)_

### Capturing performance metrics

- [- loadVideoPerformanceMetricsWithCompletionHandler:](<avsamplebuffervideorenderer/loadvideoperformancemetrics(completionhandler_).md>)

### Classes

- [Receiver](avsamplebuffervideorenderer/receiver.md)

## See Also

### Presentation

- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) — Methods you can implement to enqueue sample buffers for presentation.
- [AVSampleBufferRenderSynchronizer](avsamplebufferrendersynchronizer.md) — An object used to synchronize multiple queued sample buffers to a single timeline.
- [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) — An object that displays compressed or uncompressed video frames.
- [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) — An object used to decompress audio and play compressed or uncompressed audio.
