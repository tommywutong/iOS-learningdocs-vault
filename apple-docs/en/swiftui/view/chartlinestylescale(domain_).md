---
title: 'chartLineStyleScale(domain:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartlinestylescale(domain:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(domain:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartlinestylescale%28domain%3A%29.json'
content_hash: 'sha256:6c8a32a29f2ddf0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartLineStyleScale(domain:)

<sub>Instance Method</sub>

Configures the line style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartLineStyleScale<Domain>(domain: Domain) -> some View where Domain : ScaleDomain

```

## Parameters

- `domain` — The possible data values plotted as line styles in the chart. You can define the domain with an array for categorical values (e.g., `["A", "B", "C"]`)

## See Also

### Line style scales

- [chartLineStyleScale(_:)](<chartlinestylescale(__).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:range:)](<chartlinestylescale(domain_range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(range:)](<chartlinestylescale(range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:mapping:)](<chartlinestylescale(domain_mapping_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(mapping:)](<chartlinestylescale(mapping_).md>) — Configures the line style scale for charts.
