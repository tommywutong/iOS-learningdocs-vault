---
title: LineMark
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/linemark
source_url: 'https://developer.apple.com/documentation/charts/linemark'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/linemark.json'
content_hash: 'sha256:a4c6c3fe9e826f19'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# LineMark

<sub>Structure</sub>

Chart content that represents data using a sequence of connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@MainActor @preconcurrency struct LineMark
```

## Overview

You create a line chart by plotting a category or date property, typically with the x position, and plotting a number category, typically with the y position. The example below plots the `date` property to the x position and the `hoursOfSunshine` property to the y position using [init(x:y:)](<linemark/init(x_y_).md>):

```swift
struct MonthlyHoursOfSunshine {
    var date: Date
    var hoursOfSunshine: Double

    init(month: Int, hoursOfSunshine: Double) {
        let calendar = Calendar.autoupdatingCurrent
        self.date = calendar.date(from: DateComponents(year: 2020, month: month))!
        self.hoursOfSunshine = hoursOfSunshine
    }
}

var data: [MonthlyHoursOfSunshine] = [
    MonthlyHoursOfSunshine(month: 1, hoursOfSunshine: 74),
    MonthlyHoursOfSunshine(month: 2, hoursOfSunshine: 99),
    // ...
    MonthlyHoursOfSunshine(month: 12, hoursOfSunshine: 62)
]

var body: some View {
    Chart(data) {
        LineMark(
            x: .value("Month", $0.date),
            y: .value("Hours of Sunshine", $0.hoursOfSunshine)
        )
    }
}
```

![](../../../attachments/f5d223bb9ca48efff7a8b1d5772443a5/LineMarkSwift.LineMarkLineChart@2x.png)

<sub>Line chart with date on x-axis and hours of sunshine on y-axis. One line showing 12 points representing hours of sunshine in a month 1 74, 2 99, 3 154, 4 201, 5 247, 6 234, 7 304, 8 248, 9 197, 10 122, 11 77, 12 62.</sub>

### Plotting multiple lines

You can plot multiple lines in a chart either by explicitly specifying the `series` parameter in [init(x:y:series:)](<linemark/init(x_y_series_).md>) or by applying the [foregroundStyle(_:)](<chartcontent/foregroundstyle(__).md>) or [lineStyle(_:)](<chartcontent/linestyle(__).md>) modifiers. Line marks with the same `series` value will always be rendered together as a single line. When `series` is unspecified line marks with the same value plotted to foreground style and line style will be grouped together and plotted on their own line. The example below plots one line per distinct value in `city` and colors each line based on the `city` it represents:

```swift
struct MonthlyHoursOfSunshine {
    var city: String
    var date: Date
    var hoursOfSunshine: Double

    init(city: String, month: Int, hoursOfSunshine: Double) {
        let calendar = Calendar.autoupdatingCurrent
        self.city = city
        self.date = calendar.date(from: DateComponents(year: 2020, month: month))!
        self.hoursOfSunshine = hoursOfSunshine
    }
}

var data: [MonthlyHoursOfSunshine] = [
    MonthlyHoursOfSunshine(city: "Seattle", month: 1, hoursOfSunshine: 74),
    MonthlyHoursOfSunshine(city: "Cupertino", month: 1, hoursOfSunshine: 196),
    // ...
    MonthlyHoursOfSunshine(city: "Seattle", month: 12, hoursOfSunshine: 62),
    MonthlyHoursOfSunshine(city: "Cupertino", month: 12, hoursOfSunshine: 199)
]

var body: some View {
    Chart(data) {
        LineMark(
            x: .value("Month", $0.date),
            y: .value("Hours of Sunshine", $0.hoursOfSunshine)
        )
        .foregroundStyle(by: .value("City", $0.city))
    }
}
```

![](../../../attachments/664a5f51f8a32304b545b80911697bb0/LineMarkSwift.LineMarkMultiSeriesLineChart@2x.png)

<sub>Multi-series line chart with date on x-axis and hours of sunshine on y-axis. Two lines showing 12 points representing hours of sunshine in a month for  a city. Seattle: 1 74, 2 99, 3 154, 4 201, 5 247, 6 234, 7 304, 8 248, 9 197, 10 122, 11 77, 12 62 and Cupertino: 1 196, 2 204, 3 253, 4 288, 5 311, 6 342, 7 360, 8 331, 9 300, 10 246, 11 212, 12 199.</sub>

> [!note] Note
> Colors are repeated if the number of series is greater than the total number of colors.

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a line mark

- [init(x:y:)](<linemark/init(x_y_).md>) — Creates a line mark.
- [init(x:y:series:)](<linemark/init(x_y_series_).md>) — Creates a separate line for each unique value of series.

## See Also

### Marks

- [AreaMark](areamark.md) — Chart content that represents data using the area of one or more regions.
- [PointMark](pointmark.md) — Chart content that represents data using points.
- [RectangleMark](rectanglemark.md) — Chart content that represents data using rectangles.
- [RuleMark](rulemark.md) — Chart content that represents data using a single horizontal or vertical rule.
- [BarMark](barmark.md) — Chart content that represents data using bars.
- [SectorMark](sectormark.md) — A sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
