---
title: 'chronologicalMerge(with:_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avmetrics/chronologicalmerge(with:_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avmetrics/chronologicalmerge(with:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avmetrics/chronologicalmerge%28with%3A_%3A%29.json'
content_hash: 'sha256:bfdf8436c32e1b5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVMetrics](../avmetrics.md)

# chronologicalMerge(with:_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func chronologicalMerge<OtherSecondMetric, each MetricEventPack>(with secondMetric: AVMetrics<OtherSecondMetric>, _ metrics: repeat AVMetrics<each MetricEventPack>) -> AVMergedMetrics<MetricEvent, OtherSecondMetric, repeat each MetricEventPack> where OtherSecondMetric : AVMetricEvent, repeat each MetricEventPack : AVMetricEvent
```
