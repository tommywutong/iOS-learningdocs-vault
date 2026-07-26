---
title: 'chartForegroundStyleScale(domain:range:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartforegroundstylescale(domain:range:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartforegroundstylescale(domain:range:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartforegroundstylescale%28domain%3Arange%3Atype%3A%29.json'
content_hash: 'sha256:d8283011cebdae7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartForegroundStyleScale(domain:range:type:)

<sub>Instance Method</sub>

Configures the foreground style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartForegroundStyleScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ShapeStyle

```

## Parameters

- `domain` — The possible data values plotted as foreground style in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

- `range` — The range of foreground styles that correspond to the scale domain.

- `type` — The scale type.

## See Also

### Styles

- [chartBackground(alignment:content:)](<chartbackground(alignment_content_).md>) — Adds a background to a view that contains a chart.
- [chartForegroundStyleScale(_:)](<chartforegroundstylescale(__).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:type:)](<chartforegroundstylescale(domain_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:mapping:)](<chartforegroundstylescale(domain_mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(mapping:)](<chartforegroundstylescale(mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(range:type:)](<chartforegroundstylescale(range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(type:)](<chartforegroundstylescale(type_).md>) — Configures the foreground style scale for charts.
- [chartPlotStyle(content:)](<chartplotstyle(content_).md>) — Configures the plot area of charts.
