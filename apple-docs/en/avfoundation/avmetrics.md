---
title: AVMetrics
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetrics
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetrics.json'
content_hash: 'sha256:219ce6d2838e2bbc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetrics

<sub>Structure</sub>

An asynchronous stream of metric information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVMetrics<MetricEvent> where MetricEvent : AVMetricEvent
```

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Merging metrics

- [chronologicalMerge(with:_:)](<avmetrics/chronologicalmerge(with___).md>)

## See Also

### Metrics

- [AVMergedMetrics](avmergedmetrics.md) — An asynchronous stream of metric information from different publishers.
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
