---
title: 'foregroundStyle(by:)'
framework: Swift Charts
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/chartcontent/foregroundstyle(by:)'
source_url: 'https://developer.apple.com/documentation/charts/chartcontent/foregroundstyle(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/chartcontent/foregroundstyle%28by%3A%29.json'
content_hash: 'sha256:cfb0a97191a377fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [ChartContent](../chartcontent.md)

# foregroundStyle(by:)

<sub>Instance Method</sub>

Represents data using a foreground style.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func foregroundStyle<D>(by value: PlottableValue<D>) -> some ChartContent where D : Plottable

```

## Parameters

- `value` — The data value to encode using foreground style.

## See Also

### Encoding data into mark characteristics

- [lineStyle(by:)](<linestyle(by_).md>) — Represents data using line styles.
- [position(by:axis:span:)](<position(by_axis_span_).md>) — Represents data using position.
- [symbol(by:)](<symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(by:)](<symbolsize(by_).md>) — Represents data using symbol sizes.
