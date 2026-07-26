---
title: 'chartSymbolScale(mapping:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartsymbolscale(mapping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartsymbolscale(mapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartsymbolscale%28mapping%3A%29.json'
content_hash: 'sha256:b2375a1ed87d9071'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartSymbolScale(mapping:)

<sub>Instance Method</sub>

Configures the symbol scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartSymbolScale<DataValue, S>(mapping: @escaping (DataValue) -> S) -> some View where DataValue : Plottable, S : ChartSymbolShape

```

## Parameters

- `mapping` — Maps data categories to symbol shapes.

## See Also

### Symbol scales

- [chartSymbolScale(_:)](<chartsymbolscale(__).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(domain:)](<chartsymbolscale(domain_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:range:)](<chartsymbolscale(domain_range_).md>) — Configures the symbol style scale for charts.
- [chartSymbolScale(domain:mapping:)](<chartsymbolscale(domain_mapping_).md>) — Configures the symbol scale for charts.
- [chartSymbolScale(range:)](<chartsymbolscale(range_).md>) — Configures the symbol style scale for charts.
