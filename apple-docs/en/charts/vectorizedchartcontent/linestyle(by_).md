---
title: 'lineStyle(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/vectorizedchartcontent/linestyle(by:)'
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent/linestyle(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent/linestyle%28by%3A%29.json'
content_hash: 'sha256:f5918e944578a381'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [VectorizedChartContent](../vectorizedchartcontent.md)

# lineStyle(by:)

<sub>Instance Method</sub>

Represents data using line styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineStyle(by value: PlottableProjection<Self.DataElement, some Plottable>) -> some VectorizedChartContent<Self.DataElement>

```

## Parameters

- `value` — The keyPath accessor for the data value that encodes the line style.

## See Also

### Encoding data into mark characteristics

- [foregroundStyle(by:)](<foregroundstyle(by_).md>) — Represents data using a foreground style.
- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(by:)](<symbolsize(by_).md>) — Represents data using symbol sizes.
