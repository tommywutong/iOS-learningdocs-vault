---
title: 'init(x:yStart:yEnd:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rulemark/init(x:ystart:yend:)-5gy50'
source_url: 'https://developer.apple.com/documentation/charts/rulemark/init(x:ystart:yend:)-5gy50'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rulemark/init%28x%3Aystart%3Ayend%3A%29-5gy50.json'
content_hash: 'sha256:ecafe725c6bf048e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RuleMark](../rulemark.md)

# init(x:yStart:yEnd:)

<sub>Initializer</sub>

Creates a vertical rule mark with an x encoding and y interval encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X, Y>(x: PlottableValue<X>, yStart: PlottableValue<Y>, yEnd: PlottableValue<Y>) where X : Plottable, Y : Plottable
```

## Parameters

- `x` — The value plotted with x.

- `yStart` — The value plotted with y start.

- `yEnd` — The value plotted with y end.

### Discussion

Use this initializer to create a vertical line at y positions from `yStart` to `yEnd` to an x position:

```swift
Chart(data) {
    RuleMark(
        x: .value("Pollen Source", $0.source),
        yStart: .value("Start Date", $0.startDate),
        yEnd: .value("End Date", $0.endDate)
    )
}
```

![](../../../../attachments/8d9e636deb922381874946adc7aaaae3/LineSegmentMarkSwift.LineSegmentMarkVerticalLineSegmentChart@2x.png)

<sub>Vertical rule chart with y-axis showing the month in the year 2020 starting with January and ending with December, and with x-axis showing a pollen source: Trees, Grass, and Weeds. There are 4 rules. 2 for Trees 1 starting in January and going until the end of September and 1 spanning December, 1 for Grass starting in March and going until the end of August, and 1 for Weeds starting in April and going until the end of November.</sub>

See [RuleMark](../rulemark.md) for the setup of the structure that contains the `startDate`, `endDate`, and `source` properties.
