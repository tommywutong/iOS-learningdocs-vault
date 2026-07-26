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
doc_path: '/documentation/charts/numberbins/init(range:count:)-7975l'
source_url: 'https://developer.apple.com/documentation/charts/numberbins/init(range:count:)-7975l'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins/init%28range%3Acount%3A%29-7975l.json'
content_hash: 'sha256:2d750b2a1854e9ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [NumberBins](../numberbins.md)

# init(range:count:)

<sub>Initializer</sub>

Creates the given number of bins for the range.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(range: ClosedRange<Value>, count: Int) where Value : BinaryFloatingPoint
```

## Parameters

- `range` — The range of the bins. The first bin starts at the lower bound of the range, and the last bin ends at the upper bound of the range.

- `count` — The exact number of bins.
