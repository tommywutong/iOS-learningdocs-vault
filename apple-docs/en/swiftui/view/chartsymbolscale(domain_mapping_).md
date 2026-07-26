---
title: 'chartSymbolScale(domain:mapping:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartsymbolscale(domain:mapping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:mapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartsymbolscale%28domain%3Amapping%3A%29.json'
content_hash: 'sha256:021f931fa106f591'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartSymbolScale(domain:mapping:)

<sub>Instance Method</sub>

Configures the symbol scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartSymbolScale<Domain, S>(domain: Domain, mapping: @escaping (Domain.Element) -> S) -> some View where Domain : Collection, S : ChartSymbolShape, Domain.Element : Plottable

```

## Parameters

- `domain` — The possible data values plotted as symbol in the chart.

- `mapping` — Maps data categories to symbol shapes.

## See Also

### Symbol scales

- [chartSymbolScale(_:)](<chartsymbolscale(__).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(domain:)](<chartsymbolscale(domain_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:range:)](<chartsymbolscale(domain_range_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(mapping:)](<chartsymbolscale(mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(range:)](<chartsymbolscale(range_).md>) — Configures the symbol style scale for charts.
