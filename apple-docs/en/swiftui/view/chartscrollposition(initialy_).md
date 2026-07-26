---
title: 'chartScrollPosition(initialY:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartscrollposition(initialy:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartscrollposition(initialy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartscrollposition%28initialy%3A%29.json'
content_hash: 'sha256:c6f95ea977bcab48'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartScrollPosition(initialY:)

<sub>Instance Method</sub>

Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartScrollPosition(initialY: some Plottable) -> some View

```

## See Also

### Scrolling

- [chartScrollPosition(initialX:)](<chartscrollposition(initialx_).md>) — Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(x:)](<chartscrollposition(x_).md>) — Associates a binding to be updated when the chart scrolls along the x-axis.
- [chartScrollPosition(y:)](<chartscrollposition(y_).md>) — Associates a binding to be updated when the chart scrolls along the y-axis.
- [chartScrollTargetBehavior(_:)](<chartscrolltargetbehavior(__).md>) — Sets the scroll behavior of the scrollable chart.
- [chartScrollableAxes(_:)](<chartscrollableaxes(__).md>) — Configures the scrollable behavior of charts in this view.
