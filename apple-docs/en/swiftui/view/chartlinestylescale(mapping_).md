---
title: 'chartLineStyleScale(mapping:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartlinestylescale(mapping:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartlinestylescale(mapping:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartlinestylescale%28mapping%3A%29.json'
content_hash: 'sha256:4a14c9776cb69ae7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartLineStyleScale(mapping:)

<sub>Instance Method</sub>

Configures the line style scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartLineStyleScale<DataValue>(mapping: @escaping (DataValue) -> StrokeStyle) -> some View where DataValue : Plottable

```

## Parameters

- `mapping` — Maps data categories to line styles.

## See Also

### Line style scales

- [chartLineStyleScale(_:)](<chartlinestylescale(__).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:)](<chartlinestylescale(domain_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:range:)](<chartlinestylescale(domain_range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(range:)](<chartlinestylescale(range_).md>) — Configures the line style scale for charts.
- [chartLineStyleScale(domain:mapping:)](<chartlinestylescale(domain_mapping_).md>) — Configures the line style scale for charts.
