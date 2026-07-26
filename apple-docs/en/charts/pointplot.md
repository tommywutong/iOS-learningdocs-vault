---
title: PointPlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/pointplot
source_url: 'https://developer.apple.com/documentation/charts/pointplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/pointplot.json'
content_hash: 'sha256:8cf10fe4b9518f53'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# PointPlot

<sub>Structure</sub>

Chart content that represents a collection of data using points.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct PointPlot<Content>
```

## Overview

Use `PointPlot` when you want to visualize data in the same way as with [PointMark](pointmark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    PointPlot(
        flightDelays,
        x: .value("Flight Distance", \.distance),
        y: .value("Flight Delay", \.delay)
    )
    .foregroundStyle(by: .value("Airline", \.airline))
    .opacity(\.opacity)
    .symbolSize(by: .value("Capacity", \.passengerCount))
    .symbol(.circle)
}
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting points from a collection

- [init(_:x:y:)](<pointplot/init(__x_y_)-1a9af.md>)
- [init(_:x:y:)](<pointplot/init(__x_y_)-1p6px.md>)
- [init(_:x:y:)](<pointplot/init(__x_y_)-72pm2.md>)
- [init(_:x:y:)](<pointplot/init(__x_y_)-7frpp.md>)
- [init(_:x:y:)](<pointplot/init(__x_y_)-9p3yg.md>)

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedPointPlotContent](vectorizedpointplotcontent.md) — An opaque vectorized chart content type.

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
