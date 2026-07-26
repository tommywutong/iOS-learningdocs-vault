---
title: 'chartPlotStyle(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartplotstyle(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartplotstyle(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartplotstyle%28content%3A%29.json'
content_hash: 'sha256:580f56828fc8a015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartPlotStyle(content:)

<sub>Instance Method</sub>

Configures the plot area of charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartPlotStyle<Content>(@ViewBuilder content: @escaping (ChartPlotContent) -> Content) -> some View where Content : View

```

## Parameters

- `content` — A closure that returns the content of the plot area.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of charts.

For example:

```swift
Chart(data: data) {
    BarMark(x: .value("Category", $0.category))
}
.chartPlotStyle { content in
    content.frame(width: 100, height: 100)
}
```

## See Also

### Styles

- [chartBackground(alignment:content:)](<chartbackground(alignment_content_).md>) — Adds a background to a view that contains a chart.
- [chartForegroundStyleScale(_:)](<chartforegroundstylescale(__).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:range:type:)](<chartforegroundstylescale(domain_range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:type:)](<chartforegroundstylescale(domain_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(domain:mapping:)](<chartforegroundstylescale(domain_mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(mapping:)](<chartforegroundstylescale(mapping_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(range:type:)](<chartforegroundstylescale(range_type_).md>) — Configures the foreground style scale for charts.
- [chartForegroundStyleScale(type:)](<chartforegroundstylescale(type_).md>) — Configures the foreground style scale for charts.
