---
title: AVVideoPerformanceMetrics
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.4+, iPadOS 17.4+, Mac Catalyst 17.4+, macOS 14.4+, tvOS 17.4+, visionOS 1.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avvideoperformancemetrics
source_url: 'https://developer.apple.com/documentation/avfoundation/avvideoperformancemetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avvideoperformancemetrics.json'
content_hash: 'sha256:addb5cba0b03a822'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVVideoPerformanceMetrics

<sub>Class</sub>

An object that provides metrics related to video playback quality.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class AVVideoPerformanceMetrics
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting metrics

- [numberOfCorruptedFrames](avvideoperformancemetrics/numberofcorruptedframes.md) — The total number of corrupted frames.
- [numberOfDroppedFrames](avvideoperformancemetrics/numberofdroppedframes.md) — The total number of frames the system drops prior to decoding or from missing the display deadline.
- [numberOfFramesDisplayedUsingOptimizedCompositing](avvideoperformancemetrics/numberofframesdisplayedusingoptimizedcompositing.md) — The total number of full screen frames rendered in a special power-efficient mode that didn’t require compositing with other UI elements.
- [totalAccumulatedFrameDelay](avvideoperformancemetrics/totalaccumulatedframedelay.md) — The accumulated amount of time between the prescribed presentation times of displayed video frames and their actual time of display.
- [totalNumberOfFrames](avvideoperformancemetrics/totalnumberofframes.md) — The total number of frames that display if no frames drop.

## See Also

### Metrics

- [AVMetrics](avmetrics.md) — An asynchronous stream of metric information.
- [AVMergedMetrics](avmergedmetrics.md) — An asynchronous stream of metric information from different publishers.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
