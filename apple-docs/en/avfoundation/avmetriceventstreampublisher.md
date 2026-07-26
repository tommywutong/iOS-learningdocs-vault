---
title: AVMetricEventStreamPublisher
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avmetriceventstreampublisher
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetriceventstreampublisher'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetriceventstreampublisher.json'
content_hash: 'sha256:fa8423a2485a0fce'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVMetricEventStreamPublisher

<sub>Protocol</sub>

A type for objects that publish metric events to the event stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol AVMetricEventStreamPublisher
```

## Relationships

- **Conforming Types**: [AVPlayerItem](avplayeritem.md)

## Topics

### Getting the metrics

- [allMetrics()](<avmetriceventstreampublisher/allmetrics().md>)
- [metrics(forType:)](<avmetriceventstreampublisher/metrics(fortype_).md>)

## See Also

### Metrics

- [AVMetrics](avmetrics.md) — An asynchronous stream of metric information.
- [AVMergedMetrics](avmergedmetrics.md) — An asynchronous stream of metric information from different publishers.
- [AVVideoPerformanceMetrics](avvideoperformancemetrics.md) — An object that provides metrics related to video playback quality.
- [AVMetricEvent](avmetricevent.md) — A base class that represents a metric event.
- [AVMetricErrorEvent](avmetricerrorevent.md) — An object that represents a metric event when an error occurs.
- [Metric event types](metric-event-types.md)
