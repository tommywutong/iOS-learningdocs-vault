---
title: 'symbolSize(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/symbolsize(by:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/symbolsize(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/symbolsize%28by%3A%29.json'
content_hash: 'sha256:a4f9c3872b30578e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# symbolSize(by:)

<sub>Instance Method</sub>

Represents data using symbol sizes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func symbolSize<D>(by value: PlottableValue<D>) -> some ChartContent where D : Plottable

```

## Parameters

- `value` — The data value to encode by size.

## See Also

### Encoding data into mark characteristics

- [foregroundStyle(by:)](<foregroundstyle(by_).md>) — Represents data using a foreground style.
- [lineStyle(by:)](<linestyle(by_).md>) — Represents data using line styles.
- [position(by:axis:span:)](<position(by_axis_span_).md>) — Represents data using position.
- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
