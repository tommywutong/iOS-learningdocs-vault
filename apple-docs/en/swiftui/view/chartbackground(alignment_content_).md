---
title: 'chartBackground(alignment:content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartbackground(alignment:content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartbackground(alignment:content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartbackground%28alignment%3Acontent%3A%29.json'
content_hash: 'sha256:28020f4cd75aa722'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartBackground(alignment:content:)

<sub>Instance Method</sub>

Adds a background to a view that contains a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartBackground<V>(alignment: Alignment = .center, @ViewBuilder content: @escaping (ChartProxy) -> V) -> some View where V : View

```

## Parameters

- `alignment` — The alignment of the content.

- `content` — The content of the background.

## Discussion

You can use this modifier to define a background view as a function of the chart in the view. You can access the chart with the `ChartProxy` object passed into the closure.

> [!note] Note
> If `self` contains more than one chart, the chart proxy will refer to the first chart.

## See Also

### Styles

- [chartForegroundStyleScale(_:)](<chartforegroundstylescale(__).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:range:type:)](<chartforegroundstylescale(domain_range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:type:)](<chartforegroundstylescale(domain_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:mapping:)](<chartforegroundstylescale(domain_mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(mapping:)](<chartforegroundstylescale(mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(range:type:)](<chartforegroundstylescale(range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(type:)](<chartforegroundstylescale(type_).md>) — Configures the foreground style scale for charts.
- [chartPlotStyle(content:)](<chartplotstyle(content_).md>) — Configures the plot area of charts.
