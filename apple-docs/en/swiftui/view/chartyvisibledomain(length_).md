---
title: 'chartYVisibleDomain(length:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/chartyvisibledomain(length:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/chartyvisibledomain(length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/chartyvisibledomain%28length%3A%29.json'
content_hash: 'sha256:8399665097b0a9b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# chartYVisibleDomain(length:)

<sub>Instance Method</sub>

Sets the length of the visible domain in the Y dimension.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated func chartYVisibleDomain<P>(length: P) -> some View where P : Plottable, P : Numeric

```

## Parameters

- `length` — The length of the visible domain measured in data units. For categorical data, this should be the number of visible categories.

## Discussion

Use this method to control how much of the chart is visible in a scrollable chart. The example below sets the visible portion of the chart to 10 units in the Y axis.

```swift
Chart(data) {
    BarMark(
        x: .value("x", $0.x),
        y: .value("y", $0.y)
    )
}
.chartScrollableAxes(.vertical)
.chartYVisibleDomain(length: 10)
```

## See Also

### Visible domain

- [chartXVisibleDomain(length:)](<chartxvisibledomain(length_).md>) — Sets the length of the visible domain in the X dimension.
