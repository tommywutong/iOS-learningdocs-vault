---
title: BarPlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/barplot
source_url: 'https://developer.apple.com/documentation/charts/barplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/barplot.json'
content_hash: 'sha256:b1312b62bfb796b1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# BarPlot

<sub>Structure</sub>

Chart content that represents a collection of data using bars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct BarPlot<Content>
```

## Overview

Use `BarPlot` when you want to visualize data in the same way as with [BarMark](barmark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
BarPlot(
    votes,
    x: .value("Party", \.party),
    y: .value("Vote count", \.voteCount)
)
.foregroundStyle(by: \.partyShapeStyle)
.cornerRadius(4)
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting bars from a collection

- [init(_:x:y:width:height:stacking:)](<barplot/init(__x_y_width_height_stacking_).md>)
- [init(_:x:yStart:yEnd:width:)](<barplot/init(__x_ystart_yend_width_).md>)
- [init(_:x:yStart:yEnd:width:stacking:)](<barplot/init(__x_ystart_yend_width_stacking_)-2mtih.md>)
- [init(_:x:yStart:yEnd:width:stacking:)](<barplot/init(__x_ystart_yend_width_stacking_)-680hw.md>)
- [init(_:xStart:xEnd:y:height:stacking:)](<barplot/init(__xstart_xend_y_height_stacking_)-16tou.md>)
- [init(_:xStart:xEnd:y:height:stacking:)](<barplot/init(__xstart_xend_y_height_stacking_)-2x0yx.md>)
- [init(_:xStart:xEnd:y:height:)](<barplot/init(__xstart_xend_y_height_).md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<barplot/init(__xstart_xend_ystart_yend_)-48su5.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<barplot/init(__xstart_xend_ystart_yend_)-862wn.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<barplot/init(__xstart_xend_ystart_yend_)-mtdv.md>)
- [init(_:xStart:xEnd:yStart:yEnd:)](<barplot/init(__xstart_xend_ystart_yend_)-raqh.md>)

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedBarPlotContent](vectorizedbarplotcontent.md) — An opaque vectorized chart content type.

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
