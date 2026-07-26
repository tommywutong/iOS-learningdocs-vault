---
title: 'chartScrollPosition(y:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartscrollposition(y:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartscrollposition(y:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartscrollposition%28y%3A%29.json'
content_hash: 'sha256:f54391385a3e726b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartScrollPosition(y:)

<sub>Instance Method</sub>

Associates a binding to be updated when the chart scrolls along the y-axis.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartScrollPosition(y: Binding<some Plottable>) -> some View

```

## See Also

### Scrolling

- [chartScrollPosition(initialX:)](<chartscrollposition(initialx_).md>) — Sets the initial scroll position along the x-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(initialY:)](<chartscrollposition(initialy_).md>) — Sets the initial scroll position along the y-axis. Once the user scrolls the scroll view, the value provided to this modifier will have no effect.
- [chartScrollPosition(x:)](<chartscrollposition(x_).md>) — Associates a binding to be updated when the chart scrolls along the x-axis.
- [chartScrollTargetBehavior(_:)](<chartscrolltargetbehavior(__).md>) — Sets the scroll behavior of the scrollable chart.
- [chartScrollableAxes(_:)](<chartscrollableaxes(__).md>) — Configures the scrollable behavior of charts in this view.
