---
title: 'chartXAxisStyle(content:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartxaxisstyle(content:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartxaxisstyle(content:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartxaxisstyle%28content%3A%29.json'
content_hash: 'sha256:b9ebf1690936d3eb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartXAxisStyle(content:)

<sub>Instance Method</sub>

Configures the x axis content of charts.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartXAxisStyle<Content>(@ViewBuilder content: @escaping (ChartAxisContent) -> Content) -> some View where Content : View

```

## Parameters

- `content` — A closure that returns the content of the axis.

## Discussion

Use this modifier to configure the size or aspect ratio of the plot area of charts.

For example:

```swift
Chart(data: data) {
    BarMark(x: .value("Category", $0.category))
}
.chartXAxisStyle { axis in
    axis.opacity(0.5)
}
```

## See Also

### Axes

- [chartXAxis(_:)](<chartxaxis(__).md>) — Sets the visibility of the x axis.
- [chartXAxis(content:)](<chartxaxis(content_).md>) — Configures the x-axis for charts in the view.
- [chartYAxis(_:)](<chartyaxis(__).md>) — Sets the visibility of the y axis.
- [chartYAxis(content:)](<chartyaxis(content_).md>) — Configures the y-axis for charts in the view.
- [chartYAxisStyle(content:)](<chartyaxisstyle(content_).md>) — Configures the y axis content of charts.
- [chartZAxis(_:)](<chartzaxis(__).md>) — Sets the visibility of the z axis.
- [chartZAxis(content:)](<chartzaxis(content_).md>) — Configures the z-axis for 3D charts in the view.
