---
title: 'chartLineStyleScale(domain:mapping:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartlinestylescale(domain:mapping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(domain:mapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartlinestylescale%28domain%3Amapping%3A%29.json'
content_hash: 'sha256:034da1b6cccd9fba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartLineStyleScale(domain:mapping:)

<sub>Instance Method</sub>

Configures the line style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartLineStyleScale<Domain>(domain: Domain, mapping: @escaping (Domain.Element) -> StrokeStyle) -> some View where Domain : Collection, Domain.Element : Plottable

```

## Parameters

- `domain` — The possible data values plotted as line style in the chart.

- `mapping` — Maps data categories to line styles.

## See Also

### Line style scales

- [chartLineStyleScale(_:)](<chartlinestylescale(__).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:)](<chartlinestylescale(domain_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:range:)](<chartlinestylescale(domain_range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(range:)](<chartlinestylescale(range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(mapping:)](<chartlinestylescale(mapping_).md>) — Configures the line style scale for charts.
