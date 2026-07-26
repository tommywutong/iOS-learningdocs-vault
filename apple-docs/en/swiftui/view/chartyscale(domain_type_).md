---
title: 'chartYScale(domain:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartyscale(domain:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartyscale(domain:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartyscale%28domain%3Atype%3A%29.json'
content_hash: 'sha256:f57fef1e0b74325d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartYScale(domain:type:)

<sub>Instance Method</sub>

Configures the y scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartYScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain

```

## Parameters

- `domain` — The possible data values along the y axis in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

- `type` — The scale type.

## See Also

### Axis scales

- [chartXScale(domain:range:type:)](<chartxscale(domain_range_type_).md>) — Configures the x scale for charts.
- [chartXScale(domain:type:)](<chartxscale(domain_type_).md>) — Configures the x scale for charts.
- [chartXScale(range:type:)](<chartxscale(range_type_).md>) — Configures the x scale for charts.
- [chartXScale(type:)](<chartxscale(type_).md>) — Configures the x scale for charts.
- [chartYScale(domain:range:type:)](<chartyscale(domain_range_type_).md>) — Configures the y scale for charts.
- [chartYScale(range:type:)](<chartyscale(range_type_).md>) — Configures the y scale for charts.
- [chartYScale(type:)](<chartyscale(type_).md>) — Configures the y scale for charts.
- [chartZScale(domain:range:type:)](<chartzscale(domain_range_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(domain:type:)](<chartzscale(domain_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(range:type:)](<chartzscale(range_type_).md>) — Configures the z scale for 3D charts.
