---
title: AVAsynchronousVideoCompositionRequest
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avasynchronousvideocompositionrequest
source_url: 'https://developer.apple.com/documentation/avfoundation/avasynchronousvideocompositionrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avasynchronousvideocompositionrequest.json'
content_hash: 'sha256:493fa5f810f588c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVAsynchronousVideoCompositionRequest

<sub>Class</sub>

An object that contains information a video compositor needs to render an output pixel buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVAsynchronousVideoCompositionRequest
```

## Overview

The video compositor must adopt the [AVVideoCompositing](avvideocompositing.md) protocol.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting the request

- [compositionTime](avasynchronousvideocompositionrequest/compositiontime.md) — A time for which to compose the frame.
- [renderContext](avasynchronousvideocompositionrequest/rendercontext.md) — The rendering context of the video composition.
- [videoCompositionInstruction](avasynchronousvideocompositionrequest/videocompositioninstruction.md) — A video composition instruction that indicates how to compose the frame.

### Accessing source data

- [attach(_:to:)](<avasynchronousvideocompositionrequest/attach(__to_).md>) — Associates the pixel buffer with the specified spatial configuration.
- [- sourceFrameByTrackID:](<avasynchronousvideocompositionrequest/sourceframe(bytrackid_).md>) — Returns a source pixel buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceReadOnlyPixelBuffer(byTrackID:)](<avasynchronousvideocompositionrequest/sourcereadonlypixelbuffer(bytrackid_).md>) — Returns the source CVReadOnlyPixelBuffer for the given track ID. If the track contains tagged buffers, a pixel buffer from one of the tagged buffers will be returned.
- [sourceReadySampleBuffer(byTrackID:)](<avasynchronousvideocompositionrequest/sourcereadysamplebuffer(bytrackid_).md>) — Returns the source CMReadySampleBuffer for the given track ID.
- [- sourceSampleBufferByTrackID:](<avasynchronousvideocompositionrequest/sourcesamplebuffer(bytrackid_).md>) — Returns a source sample buffer for the track that contains the specified identifier. _(deprecated)_
- [sourceSampleDataTrackIDs](avasynchronousvideocompositionrequest/sourcesampledatatrackids-3yiab.md) — The identifiers of tracks that contain source sample data.
- [sourceTaggedDynamicBuffers(byTrackID:)](<avasynchronousvideocompositionrequest/sourcetaggeddynamicbuffers(bytrackid_).md>) — Returns the source tagged dynamic buffers for the given track ID. Returns nil if the video track does not contain tagged buffers, or if the track does not contain video. This function should only be called when supportsSourceTaggedBuffers is YES.
- [- sourceTimedMetadataByTrackID:](<avasynchronousvideocompositionrequest/sourcetimedmetadata(bytrackid_).md>) — Returns a source timed metadata group for the track that contains the specified identifier.
- [sourceTrackIDs](avasynchronousvideocompositionrequest/sourcetrackids.md) — The identifiers of tracks that contain source video.

### Finishing the request

- [- finishWithComposedVideoFrame:](<avasynchronousvideocompositionrequest/finish(withcomposedvideoframe_).md>) — Finishes the request to compose the frame. _(deprecated)_
- [finish(withComposedPixelBuffer:)](<avasynchronousvideocompositionrequest/finish(withcomposedpixelbuffer_).md>) — The method that the custom compositor calls when composition succeeds.
- [finish(withComposedTaggedBuffers:)](<avasynchronousvideocompositionrequest/finish(withcomposedtaggedbuffers_).md>) — The method that the custom compositor calls when composition succeeds.
- [- finishWithError:](<avasynchronousvideocompositionrequest/finish(with_).md>) — Finishes the request with an error.
- [- finishCancelledRequest](<avasynchronousvideocompositionrequest/finishcancelledrequest().md>) — Cancels the request to compose a video frame.

## See Also

### Rendering the composition

- [- startVideoCompositionRequest:](<avvideocompositing/startrequest(__).md>) — Directs a custom video compositor object to create a new pixel buffer composed asynchronously from a collection of sources.
- [- cancelAllPendingVideoCompositionRequests](<avvideocompositing/cancelallpendingvideocompositionrequests().md>) — Directs a custom video compositor object to cancel or finish all pending video composition requests.
