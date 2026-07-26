---
title: 'chartSymbolSizeScale(domain:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartsymbolsizescale(domain:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartsymbolsizescale(domain:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartsymbolsizescale%28domain%3Atype%3A%29.json'
content_hash: 'sha256:b1b4a6027afa0258'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartSymbolSizeScale(domain:type:)

<sub>Instance Method</sub>

Configures the symbol size scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartSymbolSizeScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain

```

## Parameters

- `domain` — The possible data values plotted as symbol sizes in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

- `type` — The scale type.

## See Also

### Symbol size scales

- [chartSymbolSizeScale(_:)](<chartsymbolsizescale(__).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:range:type:)](<chartsymbolsizescale(domain_range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(domain:mapping:)](<chartsymbolsizescale(domain_mapping_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(mapping:)](<chartsymbolsizescale(mapping_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(range:type:)](<chartsymbolsizescale(range_type_).md>) — Configures the symbol size scale for charts.
- [chartSymbolSizeScale(type:)](<chartsymbolsizescale(type_).md>) — Configures the symbol size scale for charts.
