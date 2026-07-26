---
title: 'chartZScale(domain:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartzscale(domain:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartzscale(domain:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartzscale%28domain%3Atype%3A%29.json'
content_hash: 'sha256:2e538d362d109135'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartZScale(domain:type:)

<sub>Instance Method</sub>

Configures the z scale for 3D charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func chartZScale<Domain>(domain: Domain, type: ScaleType? = nil) -> some View where Domain : ScaleDomain

```

## Parameters

- `domain` — The possible data values along the z axis in the chart. You can define the domain with a `ClosedRange` for numeric values (e.g., `0 ... 500`).

- `type` — The scale type.

## See Also

### Axis scales

- [chartXScale(domain:range:type:)](<chartxscale(domain_range_type_).md>) — Configures the x scale for charts.
- [chartXScale(domain:type:)](<chartxscale(domain_type_).md>) — Configures the x scale for charts.
- [chartXScale(range:type:)](<chartxscale(range_type_).md>) — Configures the x scale for charts.
- [chartXScale(type:)](<chartxscale(type_).md>) — Configures the x scale for charts.
- [chartYScale(domain:range:type:)](<chartyscale(domain_range_type_).md>) — Configures the y scale for charts.
- [chartYScale(domain:type:)](<chartyscale(domain_type_).md>) — Configures the y scale for charts.
- [chartYScale(range:type:)](<chartyscale(range_type_).md>) — Configures the y scale for charts.
- [chartYScale(type:)](<chartyscale(type_).md>) — Configures the y scale for charts.
- [chartZScale(domain:range:type:)](<chartzscale(domain_range_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(range:type:)](<chartzscale(range_type_).md>) — Configures the z scale for 3D charts.
