---
title: 'init(xStart:xEnd:y:)'
framework: Swift Charts
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/charts/rulemark/init(xstart:xend:y:)-6jsoi'
source_url: 'https://developer.apple.com/documentation/charts/rulemark/init(xstart:xend:y:)-6jsoi'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rulemark/init%28xstart%3Axend%3Ay%3A%29-6jsoi.json'
content_hash: 'sha256:4013c5f2cd2cb0e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RuleMark](../rulemark.md)

# init(xStart:xEnd:y:)

<sub>Initializer</sub>

Creates a horizontal rule mark that plots values on its x interval.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<X>(xStart: PlottableValue<X>, xEnd: PlottableValue<X>, y: CGFloat? = nil) where X : Plottable
```

## Parameters

- `xStart` — The value plotted with x start.

- `xEnd` — The value plotted with x end.

- `y` — The y position.   If `y` is `nil`, the rule will be centered vertically by default.

### Discussion

Use this initializer to create a horizontal rule at x positions from `xStart` to `xEnd` for a single y position:

```swift
Chart(data) {
    RuleMark(
        xStart: .value("Start Date", $0.startDate),
        xEnd: .value("End Date", $0.endDate)
    )
}
```

![](../../../../attachments/72b85015d5a997aee308bad17bac88e5/LineSegmentMarkSwift.LineSegmentMarkHorizontalSingleLineSegmentChart@2x.png)

<sub>Horizontal rule chart with x-axis showing the month in the year 2020 starting with January and ending with December, and with y-axis showing a pollen source: Trees. There are 2 rules. 1 starting in January and going until the end of September and 1 spanning December.</sub>

See the second code example in [RuleMark](../rulemark.md) for the setup of the structure that contains the `startDate`, `endDate`, and `source` properties.
