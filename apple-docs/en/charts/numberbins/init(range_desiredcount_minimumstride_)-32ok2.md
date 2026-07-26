---
title: 'init(range:desiredCount:minimumStride:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/numberbins/init(range:desiredcount:minimumstride:)-32ok2'
source_url: 'https://developer.apple.com/documentation/charts/numberbins/init(range:desiredcount:minimumstride:)-32ok2'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins/init%28range%3Adesiredcount%3Aminimumstride%3A%29-32ok2.json'
content_hash: 'sha256:75e72959c222df12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [NumberBins](../numberbins.md)

# init(range:desiredCount:minimumStride:)

<sub>Initializer</sub>

Automatically determine the bins from a range of data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(range: ClosedRange<Value>, desiredCount: Int = 10, minimumStride: Value = 0) where Value : BinaryFloatingPoint
```

## Parameters

- `range` — The range the bins should cover.

- `desiredCount` — The desired number of bins for the given data. If `nil`, infer the number automatically from data.

- `minimumStride` — The minimum allowed bin size.

## Return Value

The inferred bins.
