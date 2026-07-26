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
doc_path: '/documentation/charts/rulemark/init(xstart:xend:y:)-444cp'
source_url: 'https://developer.apple.com/documentation/charts/rulemark/init(xstart:xend:y:)-444cp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rulemark/init%28xstart%3Axend%3Ay%3A%29-444cp.json'
content_hash: 'sha256:075b48e11c0f558e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift Charts](../../charts.md) · [RuleMark](../rulemark.md)

# init(xStart:xEnd:y:)

<sub>Initializer</sub>

Creates a horizontal rule mark that plots a value on y.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated init<Y>(xStart: CGFloat? = nil, xEnd: CGFloat? = nil, y: PlottableValue<Y>) where Y : Plottable
```

## Parameters

- `xStart` — The x start position. If `xStart` is `nil` the rule will start at the leading edge of the plotting area.

- `xEnd` — The x end position. If `xEnd` is `nil` the rule will end at the trailing edge of the plotting area.

- `y` — The value plotted with y.

### Discussion

Use this initializer to create a horizontal rule across a chart’s plotting area at a y position:

```swift
Chart {
    ForEach(data) {
        BarMark(
            x: .value("Department", $0.department),
            y: .value("Profit", $0.profit)
        )
    }
    RuleMark(y: .value("Break Even Threshold", 9000))
        .foregroundStyle(.red)
}
```

![](../../../../attachments/7e451f6fe310c4757a2b567b44b30323/LineSegmentMarkSwift.LineSegmentMarkBarChartWithHorizontalLineSegmentMark@2x.png)

<sub>Vertical bar chart with x-axis showing department categories Production, Marketing, Finance, and R&D, and with y-axis ranging from 0 to 15000. There are 3 bars: Production 15000, Marketing 8000, Finance 10000. A horizontal rule mark at 9000 shows the break even threshold.</sub>

See the first code example in [RuleMark](../rulemark.md) for the setup of the structure that contains the `department` and `profit` properties.
