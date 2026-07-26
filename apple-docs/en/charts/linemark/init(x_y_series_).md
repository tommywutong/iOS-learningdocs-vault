---
title: 'init(x:y:series:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/linemark/init(x:y:series:)'
source_url: 'https://developer.apple.com/documentation/charts/linemark/init(x:y:series:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/linemark/init%28x%3Ay%3Aseries%3A%29.json'
content_hash: 'sha256:11ff15845d6d3ed8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [LineMark](../linemark.md)

# init(x:y:series:)

<sub>Initializer</sub>

Creates a separate line for each unique value of series.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y, S>(x: PlottableValue<X>, y: PlottableValue<Y>, series: PlottableValue<S>) where X : Plottable, Y : Plottable, S : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `y` — The value plotted with y.

- `series` — The value with which to split the line series by.

### Discussion

Use this initializer to create a multi-line chart from a single data source.

```swift
Chart(sunshineData) {
    LineMark(
        x: .value("Month", $0.date),
        y: .value("Hours of Sunshine", $0.hoursOfSunshine)
    )
    .foregroundStyle(by: .value("City", $0.city))
}
```

![](../../../../attachments/664a5f51f8a32304b545b80911697bb0/LineMarkSwift.LineMarkMultiSeriesLineChart@2x.png)

<sub>Multi-series line chart with date on x-axis and hours of sunshine on y-axis. Two lines showing 12 points representing hours of sunshine in a month for  a city. Seattle: 1 74, 2 99, 3 154, 4 201, 5 247, 6 234, 7 304, 8 248, 9 197, 10 122, 11 77, 12 62 and Cupertino: 1 196, 2 204, 3 253, 4 288, 5 311, 6 342, 7 360, 8 331, 9 300, 10 246, 11 212, 12 199.</sub>

## See Also

### Creating a line mark

- [init(x:y:)](<init(x_y_).md>) — Creates a line mark.
