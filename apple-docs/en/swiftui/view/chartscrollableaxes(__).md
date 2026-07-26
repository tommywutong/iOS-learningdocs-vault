---
title: 'chartScrollableAxes(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartscrollableaxes(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartscrollableaxes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartscrollableaxes%28_%3A%29.json'
content_hash: 'sha256:5c4c5d0144b016db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartScrollableAxes(_:)

<sub>Instance Method</sub>

Configures the scrollable behavior of charts in this view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartScrollableAxes(_ axes: Axis.Set) -> some View

```

## Parameters

- `axes` — The set of axes to enable scrolling.

## Discussion

Use this method to make a chart scrollable. Below is an example that makes a chart scrollable along the horizontal axis.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.horizontal)
```

> [!note] Note
> When scrolling is enabled along an axis, a default portion of the chart will be made visible. You can use the `chartXVisibleDomain` or `chartYVisibleDomain` modifiers to configure the visible domain.

## See Also

### Scrolling

- [chartScrollPosition(initialX:)](<chartscrollposition(initialx_).md>) — Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(initialY:)](<chartscrollposition(initialy_).md>) — Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(x:)](<chartscrollposition(x_).md>) — Associates a binding to be updated when the chart scrolls along the x-axis.
- [chartScrollPosition(y:)](<chartscrollposition(y_).md>) — Associates a binding to be updated when the chart scrolls along the y-axis.
- [chartScrollTargetBehavior(_:)](<chartscrolltargetbehavior(__).md>) — Sets the scroll behavior of the scrollable chart.
