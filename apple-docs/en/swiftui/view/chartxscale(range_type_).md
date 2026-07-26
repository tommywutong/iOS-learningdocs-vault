---
title: 'chartXScale(range:type:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartxscale(range:type:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartxscale(range:type:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartxscale%28range%3Atype%3A%29.json'
content_hash: 'sha256:1adaf15cd6218e57'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartXScale(range:type:)

<sub>Instance Method</sub>

Configures the x scale for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartXScale<Range>(range: Range, type: ScaleType? = nil) -> some View where Range : PositionScaleRange

```

## Parameters

- `range` — The range of x positions that correspond to the scale domain. By default the range is determined by the dimension of the plot area. You can use `range: .plotDimension(startPadding:, endPadding:)` to add padding to the scale range.

- `type` — The scale type.

## See Also

### Axis scales

- [chartXScale(domain:range:type:)](<chartxscale(domain_range_type_).md>) — Configures the x scale for charts.
- [chartXScale(domain:type:)](<chartxscale(domain_type_).md>) — Configures the x scale for charts.
- [chartXScale(type:)](<chartxscale(type_).md>) — Configures the x scale for charts.
- [chartYScale(domain:range:type:)](<chartyscale(domain_range_type_).md>) — Configures the y scale for charts.
- [chartYScale(domain:type:)](<chartyscale(domain_type_).md>) — Configures the y scale for charts.
- [chartYScale(range:type:)](<chartyscale(range_type_).md>) — Configures the y scale for charts.
- [chartYScale(type:)](<chartyscale(type_).md>) — Configures the y scale for charts.
- [chartZScale(domain:range:type:)](<chartzscale(domain_range_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(domain:type:)](<chartzscale(domain_type_).md>) — Configures the z scale for 3D charts.
- [chartZScale(range:type:)](<chartzscale(range_type_).md>) — Configures the z scale for 3D charts.
