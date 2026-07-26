---
title: 'chartSymbolScale(domain:range:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartsymbolscale(domain:range:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(domain:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartsymbolscale%28domain%3Arange%3A%29.json'
content_hash: 'sha256:ff397929f435e240'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartSymbolScale(domain:range:)

<sub>Instance Method</sub>

Configures the symbol style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartSymbolScale<Domain, Range>(domain: Domain, range: Range) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue : ChartSymbolShape

```

## Parameters

- `domain` — The possible data values plotted as symbols in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

- `range` — The range of symbols that correspond to the scale domain.

## See Also

### Symbol scales

- [chartSymbolScale(_:)](<chartsymbolscale(__).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(domain:)](<chartsymbolscale(domain_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:mapping:)](<chartsymbolscale(domain_mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(mapping:)](<chartsymbolscale(mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(range:)](<chartsymbolscale(range_).md>) — Configures the symbol style scale for charts.
