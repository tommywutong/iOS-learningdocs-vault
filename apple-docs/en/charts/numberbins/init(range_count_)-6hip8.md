---
title: 'init(range:count:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/numberbins/init(range:count:)-6hip8'
source_url: 'https://developer.apple.com/documentation/charts/numberbins/init(range:count:)-6hip8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins/init%28range%3Acount%3A%29-6hip8.json'
content_hash: 'sha256:727c2e405f64437e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [NumberBins](../numberbins.md)

# init(range:count:)

<sub>Initializer</sub>

Creates the given number of bins for the range. Expects that the range length is a multiple of `count` to allow uniform integer bins.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(range: ClosedRange<Value>, count: Int) where Value : BinaryInteger
```

## Parameters

- `range` — The range of the bins. The first bin starts at the lower bound of the range, and the last bin ends at the upper bound of the range.

- `count` — The exact number of bins.
