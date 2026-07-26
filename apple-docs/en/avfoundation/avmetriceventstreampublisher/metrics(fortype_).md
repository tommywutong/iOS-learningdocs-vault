---
title: 'metrics(forType:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetriceventstreampublisher/metrics(fortype:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetriceventstreampublisher/metrics(fortype:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetriceventstreampublisher/metrics%28fortype%3A%29.json'
content_hash: 'sha256:033d1737629d8043'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetricEventStreamPublisher](../avmetriceventstreampublisher.md)

# metrics(forType:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func metrics<MetricEvent>(forType metricType: MetricEvent.Type) -> AVMetrics<MetricEvent> where MetricEvent : AVMetricEvent
```

## See Also

### Getting the metrics

- [allMetrics()](<allmetrics().md>)
