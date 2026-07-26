---
title: 'init(x:y:stacking:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/areamark/init(x:y:stacking:)'
source_url: 'https://developer.apple.com/documentation/charts/areamark/init(x:y:stacking:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areamark/init%28x%3Ay%3Astacking%3A%29.json'
content_hash: 'sha256:01d081da66c0713d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [AreaMark](../areamark.md)

# init(x:y:stacking:)

<sub>Initializer</sub>

Creates an area mark using the specified horizontal and vertical positions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, y: PlottableValue<Y>, stacking: MarkStackingMethod = .standard) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The horizontal position for the mark.

- `y` — The vertical position for the mark.

- `stacking` — The way in which the chart stacks area regions. The default is [standard](../markstackingmethod/standard.md).

## Discussion

You can use this initializer to create a basic area chart:

```swift
Chart(cheeseburgerCost) { cost in
    AreaMark(
        x: .value("Date", cost.date),
        y: .value("Price", cost.price)
    )
}
```

The resulting chart automatically scales and labels the axes based on the data, and fills the area under the data points with a default color:

![](../../../../attachments/36b91667605910cb6256e819437543de/AreaMark-1-macOS@2x.png)

<sub>A chart that shows the years 1960 to 2020 on the x-axis and a number in the range of 0 to 1.5 on the y-axis. An irregular, monotonically increasing, piecewise linear curve starts near the lower left and continues toward the upper right. The area under the curve is filled in with a blue color.</sub>

## See Also

### Creating an area mark

- [init(x:y:series:stacking:)](<init(x_y_series_stacking_).md>) — Creates an area mark and associates it with the specified series.
