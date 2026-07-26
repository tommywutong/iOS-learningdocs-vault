---
title: SectorPlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/sectorplot
source_url: 'https://developer.apple.com/documentation/charts/sectorplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/sectorplot.json'
content_hash: 'sha256:2926f2485bd5b315'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# SectorPlot

<sub>Structure</sub>

Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SectorPlot<Content>
```

## Overview

Use `SectorPlot` when you want to visualize data in the same way as with [SectorMark](sectormark.md), but you want to visualize an entire data collection with a single plot.

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
SectorPlot(
    votes,
    angle: .value("Vote count", \.voteCount),
    angularInset: 1
)
.foregroundStyle(by: .value("Party", \.party))
.cornerRadius(4)
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting sectors from a collection

- [init(_:angle:innerRadius:outerRadius:angularInset:)](<sectorplot/init(__angle_innerradius_outerradius_angularinset_)-1ed01.md>)
- [init(_:angle:innerRadius:outerRadius:angularInset:)](<sectorplot/init(__angle_innerradius_outerradius_angularinset_)-9pmo7.md>)

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedSectorPlotContent](vectorizedsectorplotcontent.md) — An opaque vectorized chart content type.

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
