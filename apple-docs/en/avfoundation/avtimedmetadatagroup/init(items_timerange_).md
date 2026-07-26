---
title: 'init(items:timeRange:)'
framework: AVFoundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.3+, iPadOS 4.3+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avtimedmetadatagroup/init(items:timerange:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avtimedmetadatagroup/init(items:timerange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avtimedmetadatagroup/init%28items%3Atimerange%3A%29.json'
content_hash: 'sha256:82cb58191b14d596'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVTimedMetadataGroup](../avtimedmetadatagroup.md)

# init(items:timeRange:)

<sub>Initializer</sub>

Creates a timed metadata group initialized with the given metadata items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(items: [AVMetadataItem], timeRange: CMTimeRange)
```

## Parameters

- `items` — An array of [AVMetadataItem](../avmetadataitem.md) objects.

- `timeRange` — The time range of the metadata contained in `items`.

## Return Value

A metadata group initialized with `items`.

## See Also

### Creating a timed metadata group

- [init(sampleBuffer:)](<init(samplebuffer_)-6atlv.md>) — Creates a timed metadata group with a sample buffer.
- [- initWithSampleBuffer:](<init(samplebuffer_)-bjuo.md>) _(deprecated)_
