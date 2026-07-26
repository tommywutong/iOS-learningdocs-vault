---
title: 'chartScrollTargetBehavior(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartscrolltargetbehavior(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartscrolltargetbehavior(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartscrolltargetbehavior%28_%3A%29.json'
content_hash: 'sha256:a14d88569c1092f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartScrollTargetBehavior(_:)

<sub>Instance Method</sub>

Sets the scroll behavior of the scrollable chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartScrollTargetBehavior(_ behavior: some ChartScrollTargetBehavior) -> some View

```

## Parameters

- `behavior` — The chart scroll target behavior.

## Discussion

Use this method to control how the chart scrolls and aligns when the user finishes scrolling. The example below sets the scroll target behavior to align to the values in the chart. When the user finishes scrolling, the chart will settle to align with the values in the chart.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.vertical)
.chartYVisibleDomain(length: 10)
.chartScrollTargetBehavior(.valueAligned(unit: 1))
```

## See Also

### Scrolling

- [chartScrollPosition(initialX:)](<chartscrollposition(initialx_).md>) — Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(initialY:)](<chartscrollposition(initialy_).md>) — Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(x:)](<chartscrollposition(x_).md>) — Associates a binding to be updated when the chart scrolls along the x-axis.
- [chartScrollPosition(y:)](<chartscrollposition(y_).md>) — Associates a binding to be updated when the chart scrolls along the y-axis.
- [chartScrollableAxes(_:)](<chartscrollableaxes(__).md>) — Configures the scrollable behavior of charts in this view.
