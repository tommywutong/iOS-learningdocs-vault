---
title: 'symbol(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/symbol(by:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbol(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/symbol%28by%3A%29.json'
content_hash: 'sha256:cc39d44c1cb65318'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# symbol(by:)

<sub>Instance Method</sub>

Represents data using different kinds of symbols.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbol(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `value` — The data value. `value` must be categorial, such as `String`.

## See Also

### Setting symbol appearance

- [symbolSize(_:)](<symbolsize(__)-12tl1.md>) — Sets the plotting symbol size for the chart content.
- [symbolSize(_:)](<symbolsize(__)-3nwop.md>) — Sets the plotting symbol size for the chart content according to a perceived area.
