---
title: 'init(data:desiredCount:minimumStride:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/numberbins/init(data:desiredcount:minimumstride:)-8pvv7'
source_url: 'https://developer.apple.com/documentation/charts/numberbins/init(data:desiredcount:minimumstride:)-8pvv7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/numberbins/init%28data%3Adesiredcount%3Aminimumstride%3A%29-8pvv7.json'
content_hash: 'sha256:5a6eff0d8f83d671'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [NumberBins](../numberbins.md)

# init(data:desiredCount:minimumStride:)

<sub>Initializer</sub>

Automatically determine the bins from data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init(data: [Value], desiredCount: Int? = nil, minimumStride: Value = 0) where Value : BinaryInteger
```

## Parameters

- `data` — The given data values.

- `desiredCount` — The desired number of bins for the given data. If `nil`, infer the number of bins automatically from data using [Scott’s normal reference rule](https://doi.org/10.1093/biomet/66.3.605) capped at 200.

- `minimumStride` — The minimum allowed bin size.

## Return Value

The inferred bins.
