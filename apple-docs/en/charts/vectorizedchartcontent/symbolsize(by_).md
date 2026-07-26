---
title: 'symbolSize(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/symbolsize(by:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/symbolsize(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/symbolsize%28by%3A%29.json'
content_hash: 'sha256:5fefda54c99e34f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# symbolSize(by:)

<sub>Instance Method</sub>

Represents data using symbol sizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbolSize(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `value` — The data value to encode by size.

## See Also

### Encoding data into mark characteristics

- [foregroundStyle(by:)](<foregroundstyle(by_).md>) — Represents data using a foreground style.
- [lineStyle(by:)](<linestyle(by_).md>) — Represents data using line styles.
- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
