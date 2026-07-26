---
title: RectanglePlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/rectangleplot
source_url: 'https://developer.apple.com/documentation/charts/rectangleplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/rectangleplot.json'
content_hash: 'sha256:721c6156c4bbb033'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# RectanglePlot

<sub>Structure</sub>

Chart content that represents a collection of data using rectangles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RectanglePlot<Content>
```

## Overview

Use `RectanglePlot` when you want to visualize data in the same way as with [RectangleMark](rectanglemark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    RectanglePlot(
        tasks,
        x: .value("Time", \.startTime, \.endTime),
        y: .value("Project", \.project)
    )
    .foregroundStyle(by: .value("Status", \.status))
    .cornerRadius(4)
}
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting rectangles from a collection

- [init(_:x:y:width:height:)](<rectangleplot/init(__x_y_width_height_).md>)
- [init(_:x:yStart:yEnd:width:)](<rectangleplot/init(__x_ystart_yend_width_)-93op1.md>)
- [init(_:x:yStart:yEnd:width:)](<rectangleplot/init(__x_ystart_yend_width_)-nnvk.md>)
- [init(_:x:yStart:yEnd:width:)](<rectangleplot/init(__x_ystart_yend_width_)-12u1b.md>)
- [init(_:xStart:xEnd:y:height:)](<rectangleplot/init(__xstart_xend_y_height_)-51nra.md>)
- [init(_:xStart:xEnd:y:height:)](<rectangleplot/init(__xstart_xend_y_height_)-8s17v.md>)
- [init(_:xStart:xEnd:y:height:)](<rectangleplot/init(__xstart_xend_y_height_)-15ish.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-46wi0.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-4g377.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-6d8yb.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-6uuk4.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-741lz.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<rectangleplot/init(__xstart_xend_ystart_yend_)-ir9o.md>)

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedRectanglePlotContent](vectorizedrectangleplotcontent.md) — An opaque vectorized chart content type.

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
