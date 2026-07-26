---
title: 'chartZAxis(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, visionOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartzaxis(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartzaxis(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartzaxis%28content%3A%29.json'
content_hash: 'sha256:ed73792673261eed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartZAxis(content:)

<sub>Instance Method</sub>

Configures the z-axis for 3D charts in the view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func chartZAxis<Content>(@AxisContentBuilder content: () -> Content) -> some View where Content : AxisContent

```

## Parameters

- `content` — The axis content.

## Discussion

Use this modifier to customize the z-axis of a chart. Provide an `AxisMarks` builder that composes `AxisGridLine`, `AxisTick`, and `AxisValueLabel` structures to form the axis. Omit components from the builder to omit them from the resulting axis. For example, the following code adds grid lines to the z-axis:

```swift
.chartZAxis {
    AxisMarks {
        AxisGridLine()
    }
}
```

Use arguments such as `position:` or `values:` to control the placement of the axis values it displays.

> [!note] Note
> To add an axis label, use one of the label modifiers, like doc://com.apple.documentation/documentation/SwiftUI/View/chartZAxisLabel(position:alignment:spacing:content:).

## See Also

### Axes

- [chartXAxis(_:)](<chartxaxis(__).md>) — Sets the visibility of the x axis.
- [chartXAxis(content:)](<chartxaxis(content_).md>) — Configures the x-axis for charts in the view.
- [chartXAxisStyle(content:)](<chartxaxisstyle(content_).md>) — Configures the x axis content of charts.
- [chartYAxis(_:)](<chartyaxis(__).md>) — Sets the visibility of the y axis.
- [chartYAxis(content:)](<chartyaxis(content_).md>) — Configures the y-axis for charts in the view.
- [chartYAxisStyle(content:)](<chartyaxisstyle(content_).md>) — Configures the y axis content of charts.
- [chartZAxis(_:)](<chartzaxis(__).md>) — Sets the visibility of the z axis.
