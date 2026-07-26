---
title: 'chartLineStyleScale(domain:range:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartlinestylescale(domain:range:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(domain:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartlinestylescale%28domain%3Arange%3A%29.json'
content_hash: 'sha256:ec19086430bca517'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartLineStyleScale(domain:range:)

<sub>Instance Method</sub>

Configures the line style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartLineStyleScale<Domain, Range>(domain: Domain, range: Range) -> some View where Domain : ScaleDomain, Range : ScaleRange, Range.VisualValue == StrokeStyle

```

## Parameters

- `domain` — The possible data values plotted as line styles in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

- `range` — The range of line styles that correspond to the scale domain.

## See Also

### Line style scales

- [chartLineStyleScale(_:)](<chartlinestylescale(__).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:)](<chartlinestylescale(domain_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(range:)](<chartlinestylescale(range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:mapping:)](<chartlinestylescale(domain_mapping_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(mapping:)](<chartlinestylescale(mapping_).md>) — Configures the line style scale for charts.
