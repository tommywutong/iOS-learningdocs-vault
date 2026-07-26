---
title: RulePlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/ruleplot
source_url: 'https://developer.apple.com/documentation/charts/ruleplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/ruleplot.json'
content_hash: 'sha256:bd2e0ff2727302e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# RulePlot

<sub>Structure</sub>

Chart content that represents a collection of data using a single horizontal or vertical rule.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RulePlot<Content>
```

## Overview

Use `RulePlot` when you want to visualize data in the same way as with [RuleMark](rulemark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    RulePlot(
        tasks,
        xStart: .value("Start time", \.startTime),
        xEnd: .value("End time", \.endTime),
        y: .value("Project", \.project)
    )
    .foregroundStyle(by: .value("Status", \.status))
    .opacity(\.opacity)
    .lineStyle(StrokeStyle(lineWidth: 8, lineCap: .round))
}
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting rules from a collection

- [init(_:x:yStart:yEnd:)](<ruleplot/init(__x_ystart_yend_)-13wts.md>)
- [init(_:x:yStart:yEnd:)](<ruleplot/init(__x_ystart_yend_)-3fig9.md>)
- [init(_:x:yStart:yEnd:)](<ruleplot/init(__x_ystart_yend_)-6ts7e.md>)
- [init(_:x:yStart:yEnd:)](<ruleplot/init(__x_ystart_yend_)-8b2lx.md>)
- [init(_:x:yStart:yEnd:)](<ruleplot/init(__x_ystart_yend_)-zxo0.md>)
- [init(_:xStart:xEnd:y:)](<ruleplot/init(__xstart_xend_y_)-3dsvn.md>)
- [init(_:xStart:xEnd:y:)](<ruleplot/init(__xstart_xend_y_)-4yxo8.md>)
- [init(_:xStart:xEnd:y:)](<ruleplot/init(__xstart_xend_y_)-54gxx.md>)
- [init(_:xStart:xEnd:y:)](<ruleplot/init(__xstart_xend_y_)-8ehr7.md>)
- [init(_:xStart:xEnd:y:)](<ruleplot/init(__xstart_xend_y_)-hx5a.md>)

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedRulePlotContent](vectorizedruleplotcontent.md) — An opaque vectorized chart content type.

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
