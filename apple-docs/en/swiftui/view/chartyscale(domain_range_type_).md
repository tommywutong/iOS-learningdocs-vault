---
title: 'chartYScale(domain:range:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartyscale(domain:range:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartyscale(domain:range:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartyscale%28domain%3Arange%3Atype%3A%29.json'
content_hash: 'sha256:565eaaef145a9250'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartYScale(domain:range:type:)

<sub>Instance Method</sub>

Configures the y scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartYScale<Domain, Range>(domain: Domain, range: Range, type: ScaleType? = nil) -> some View where Domain : ScaleDomain, Range : PositionScaleRange

```

## Parameters

- `domain` — The possible data values along the y axis in the chart. You can define the domain with a `ClosedRange` for number or `Date` values (e.g., `0 ... 500`), and with an array for categorical values (e.g., `["A", "B", "C"]`)

- `range` — The range of y positions that correspond to the scale domain. By default the range is determined by the dimension of the plot area. You can use `range: .plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

- `type` — The scale type.

## See Also

### Axis scales

- [chartXScale(domain:range:type:)](<chartxscale(domain_range_type_).md>) — Configures the x scale for charts.
- [chartXScale(domain:type:)](<chartxscale(domain_type_).md>) — Configures the x scale for charts.
- [chartXScale(range:type:)](<chartxscale(range_type_).md>) — Configures the x scale for charts.
- [chartXScale(type:)](<chartxscale(type_).md>) — Configures the x scale for charts.
- [chartYScale(domain:type:)](<chartyscale(domain_type_).md>) — Configures the y scale for charts.
- [chartYScale(range:type:)](<chartyscale(range_type_).md>) — Configures the y scale for charts.
- [chartYScale(type:)](<chartyscale(type_).md>) — Configures the y scale for charts.
- [chartZScale(domain:range:type:)](<chartzscale(domain_range_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(domain:type:)](<chartzscale(domain_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(range:type:)](<chartzscale(range_type_).md>) — Configures the z scale for 3D charts.
