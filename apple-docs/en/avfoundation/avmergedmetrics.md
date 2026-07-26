---
title: AVMergedMetrics
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmergedmetrics
source_url: 'https://developer.apple.com/documentation/avfoundation/avmergedmetrics'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmergedmetrics.json'
content_hash: 'sha256:819f0dd85ac5aa96'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMergedMetrics

<sub>Structure</sub>

An asynchronous stream of metric information from different publishers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AVMergedMetrics<MetricEvent1, MetricEvent2, each MetricEventPack> where MetricEvent1 : AVMetricEvent, MetricEvent2 : AVMetricEvent, repeat each MetricEventPack : AVMetricEvent
```

## Relationships

- **Conforms To**: [AsyncSequence](../swift/asyncsequence.md)

## See Also

### Metrics

- [AVMetrics](avmetrics.md) — An asynchronous stream of metric information.
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEventStreamPublisher](avmetriceventstreampublisher.md) — A type for objects that publish metric events to the event stream.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
