---
title: 'chartSymbolSizeScale(domain:mapping:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartsymbolsizescale(domain:mapping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartsymbolsizescale(domain:mapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartsymbolsizescale%28domain%3Amapping%3A%29.json'
content_hash: 'sha256:6889babc03c19c72'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartSymbolSizeScale(domain:mapping:)

<sub>Instance Method</sub>

Configures the symbol size scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartSymbolSizeScale<Domain>(domain: Domain, mapping: @escaping (Domain.Element) -> CGFloat) -> some View where Domain : Collection, Domain.Element : Plottable

```

## Parameters

- `domain` — The possible data values plotted as symbol size in the chart.

- `mapping` — Maps data categories to symbol sizes.

## See Also

### Symbol size scales

- [chartSymbolSizeScale(_:)](<chartsymbolsizescale(__).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:range:type:)](<chartsymbolsizescale(domain_range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:type:)](<chartsymbolsizescale(domain_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(mapping:)](<chartsymbolsizescale(mapping_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(range:type:)](<chartsymbolsizescale(range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(type:)](<chartsymbolsizescale(type_).md>) — Configures the symbol size scale for charts.
