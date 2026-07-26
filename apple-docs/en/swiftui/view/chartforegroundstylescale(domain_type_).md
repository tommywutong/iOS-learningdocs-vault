---
title: 'chartForegroundStyleScale(domain:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartforegroundstylescale(domain:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartforegroundstylescale(domain:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartforegroundstylescale%28domain%3Atype%3A%29.json'
content_hash: 'sha256:41cd54b11017a29c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartForegroundStyleScale(domain:type:)

<sub>Instance Method</sub>

Configures the foreground style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartForegroundStyleScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain

```

## Parameters

- `domain` — The possible data values plotted as foreground style in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

- `type` — The scale type.

## See Also

### Styles

- [chartBackground(alignment:content:)](<chartbackground(alignment_content_).md>) — Adds a background to a view that contains a chart.
- [chartForegroundStyleScale(_:)](<chartforegroundstylescale(__).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:range:type:)](<chartforegroundstylescale(domain_range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:mapping:)](<chartforegroundstylescale(domain_mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(mapping:)](<chartforegroundstylescale(mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(range:type:)](<chartforegroundstylescale(range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(type:)](<chartforegroundstylescale(type_).md>) — Configures the foreground style scale for charts.
- [chartPlotStyle(content:)](<chartplotstyle(content_).md>) — Configures the plot area of charts.
