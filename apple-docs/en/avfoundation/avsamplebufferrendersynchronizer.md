---
title: AVSampleBufferRenderSynchronizer
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avsamplebufferrendersynchronizer
source_url: 'https://developer.apple.com/documentation/avfoundation/avsamplebufferrendersynchronizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avsamplebufferrendersynchronizer.json'
content_hash: 'sha256:e71cb3e39e65be5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVSampleBufferRenderSynchronizer

<sub>Class</sub>

An object used to synchronize multiple queued sample buffers to a single timeline.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class AVSampleBufferRenderSynchronizer
```

## Overview

This class synchronizes multiple objects that conform to [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) to a single timeline.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing renderers

- [renderers](avsamplebufferrendersynchronizer/renderers.md) — An array of queued sample buffer renderers currently attached to the synchronizer. _(deprecated)_
- [- addRenderer:](<avsamplebufferrendersynchronizer/addrenderer(__).md>) — Adds a renderer to the list of renderers under the synchronizer’s control. _(deprecated)_
- [- removeRenderer:atTime:completionHandler:](<avsamplebufferrendersynchronizer/removerenderer(__at_completionhandler_).md>) — Removes a renderer from the synchronizer. _(deprecated)_

### Accessing time information

- [- currentTime](<avsamplebufferrendersynchronizer/currenttime().md>) — Returns the current time of the synchronizer.
- [timebase](avsamplebufferrendersynchronizer/timebase.md) — The synchronizer’s rendering timebase which determines how it interprets timestamps.
- [rate](avsamplebufferrendersynchronizer/rate.md) — The current playback rate.
- [- setRate:time:](<avsamplebufferrendersynchronizer/setrate(__time_).md>) — Sets the renderer’s time and rate.
- [- setRate:time:atHostTime:](<avsamplebufferrendersynchronizer/setrate(__time_athosttime_).md>) — Sets the playback rate and the relationship between the current time and host time.
- [AVSampleBufferRenderSynchronizerRateDidChangeNotification](avsamplebufferrendersynchronizer/ratedidchangenotification.md) — The synchronizer’s rendering rate changed.
- [delaysRateChangeUntilHasSufficientMediaData](avsamplebufferrendersynchronizer/delaysratechangeuntilhassufficientmediadata.md) — A Boolean value that Indicates whether the playback should start immediately on rate change requests.

### Observing time

- [- addPeriodicTimeObserverForInterval:queue:usingBlock:](<avsamplebufferrendersynchronizer/addperiodictimeobserver(forinterval_queue_using_).md>) — Requests invocation of a block during rendering at specified time intervals.
- [- addBoundaryTimeObserverForTimes:queue:usingBlock:](<avsamplebufferrendersynchronizer/addboundarytimeobserver(fortimes_queue_using_).md>) — Requests invocation of a block when specified times are traversed during normal rendering.
- [- removeTimeObserver:](<avsamplebufferrendersynchronizer/removetimeobserver(__).md>) — Cancels the specified time observer.

### Configuring audio behavior

- [intendedSpatialAudioExperience](avsamplebufferrendersynchronizer/intendedspatialaudioexperience-3z7d3.md) — The synchronizer’s intended Spatial Audio experience.

### Instance Methods

- [removeReceiver(_:at:)](<avsamplebufferrendersynchronizer/removereceiver(__at_)-3rrnp.md>) — Removes a receiver and its renderer from the synchronizer.
- [removeReceiver(_:at:)](<avsamplebufferrendersynchronizer/removereceiver(__at_)-3yxub.md>) — Removes a receiver and its renderer from the synchronizer.
- [sampleBufferReceiver(adding:)](<avsamplebufferrendersynchronizer/samplebufferreceiver(adding_)-5dw84.md>) — Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.
- [sampleBufferReceiver(adding:)](<avsamplebufferrendersynchronizer/samplebufferreceiver(adding_)-rxap.md>) — Adds a renderer to the list of renderers under the synchronizer’s control and returns a sample buffer receiver to enqueue samples.

## See Also

### Presentation

- [AVQueuedSampleBufferRendering](avqueuedsamplebufferrendering.md) — Methods you can implement to enqueue sample buffers for presentation.
- [AVSampleBufferDisplayLayer](avsamplebufferdisplaylayer.md) — An object that displays compressed or uncompressed video frames.
- [AVSampleBufferVideoRenderer](avsamplebuffervideorenderer.md) — An object that enqueues video sample buffers for rendering.
- [AVSampleBufferAudioRenderer](avsamplebufferaudiorenderer.md) — An object used to decompress audio and play compressed or uncompressed audio.
