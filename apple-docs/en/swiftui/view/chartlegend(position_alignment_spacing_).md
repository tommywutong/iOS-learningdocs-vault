---
title: 'chartLegend(position:alignment:spacing:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartlegend(position:alignment:spacing:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartlegend(position:alignment:spacing:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartlegend%28position%3Aalignment%3Aspacing%3A%29.json'
content_hash: 'sha256:5e738c99d88bc1b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartLegend(position:alignment:spacing:)

<sub>Instance Method</sub>

Configures the legend for charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency func chartLegend(position: AnnotationPosition = .automatic, alignment: Alignment? = nil, spacing: CGFloat? = nil) -> some View

```

## Parameters

- `position` — Configures the position of the legend.

- `alignment` — Alignment of the legend within the space available to it. Use `nil` for default alignment.

- `spacing` — Distance between the legend and the chart. Use `nil` for the default spacing.

## See Also

### Legends

- [chartLegend(_:)](<chartlegend(__).md>) — Configures the legend for charts.
- [chartLegend(position:alignment:spacing:content:)](<chartlegend(position_alignment_spacing_content_).md>) — Configures the legend for charts.
