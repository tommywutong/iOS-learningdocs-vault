---
title: 'lineStyle(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/linestyle(by:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/linestyle(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/linestyle%28by%3A%29.json'
content_hash: 'sha256:8bdf57e3f0778af5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# lineStyle(by:)

<sub>Instance Method</sub>

Represents data using line styles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func lineStyle<D>(by value: PlottableValue<D>) -> some ChartContent where D : Plottable

```

## Parameters

- `value` — The data value.

## See Also

### Encoding data into mark characteristics

- [foregroundStyle(by:)](<foregroundstyle(by_).md>) — Represents data using a foreground style.
- [position(by:axis:span:)](<position(by_axis_span_).md>) — Represents data using position.
- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(by:)](<symbolsize(by_).md>) — Represents data using symbol sizes.
