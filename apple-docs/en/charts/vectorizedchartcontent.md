---
title: VectorizedChartContent
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/vectorizedchartcontent
source_url: 'https://developer.apple.com/documentation/charts/vectorizedchartcontent'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/vectorizedchartcontent.json'
content_hash: 'sha256:8098f6d09db92afb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# VectorizedChartContent

<sub>Protocol</sub>

A generic type that represents content conveyed via a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol VectorizedChartContent<DataElement> : ChartContent
```

## Overview

Its primary associated type represents the data element, sometimes called _data point_, _observation_ or _aggregate_.

Usually, `DataElement` has properties to determine visual attributes directly, or indirectly by encoding `Plottable` values through a chart scale.

## Relationships

- **Inherits From**: [ChartContent](chartcontent.md)

- **Conforming Types**: [AreaPlot](areaplot.md), [BarPlot](barplot.md), [LinePlot](lineplot.md), [PointPlot](pointplot.md), [RectanglePlot](rectangleplot.md), [RulePlot](ruleplot.md), [SectorPlot](sectorplot.md), [VectorizedAreaPlotContent](vectorizedareaplotcontent.md), [VectorizedBarPlotContent](vectorizedbarplotcontent.md), [VectorizedLinePlotContent](vectorizedlineplotcontent.md), [VectorizedPointPlotContent](vectorizedpointplotcontent.md), [VectorizedRectanglePlotContent](vectorizedrectangleplotcontent.md), [VectorizedRulePlotContent](vectorizedruleplotcontent.md), [VectorizedSectorPlotContent](vectorizedsectorplotcontent.md)

## Topics

### Styling marks

- [foregroundStyle(_:)](<vectorizedchartcontent/foregroundstyle(__).md>) — Represents data using a foreground style.
- [opacity(_:)](<vectorizedchartcontent/opacity(__).md>)
- [lineStyle(_:)](<vectorizedchartcontent/linestyle(__).md>) — Represents data using line styles.
- [position(by:axis:span:)](<vectorizedchartcontent/position(by_axis_span_).md>)

### Setting symbol appearance

- [symbol(by:)](<vectorizedchartcontent/symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(_:)](<vectorizedchartcontent/symbolsize(__)-12tl1.md>) — Sets the plotting symbol size for the chart content.
- [symbolSize(_:)](<vectorizedchartcontent/symbolsize(__)-3nwop.md>) — Sets the plotting symbol size for the chart content according to a perceived area.

### Encoding data into mark characteristics

- [foregroundStyle(by:)](<vectorizedchartcontent/foregroundstyle(by_).md>) — Represents data using a foreground style.
- [lineStyle(by:)](<vectorizedchartcontent/linestyle(by_).md>) — Represents data using line styles.
- [symbol(by:)](<vectorizedchartcontent/symbol(by_).md>) — Represents data using different kinds of symbols.
- [symbolSize(by:)](<vectorizedchartcontent/symbolsize(by_).md>) — Represents data using symbol sizes.

### Configuring accessibility

- [accessibilityHidden(_:)](<vectorizedchartcontent/accessibilityhidden(__).md>) — Specifies whether to hide this chart content from system accessibility features.
- [accessibilityIdentifier(_:)](<vectorizedchartcontent/accessibilityidentifier(__).md>) — Adds an identifier string to the chart content.
- [accessibilityLabel(_:)](<vectorizedchartcontent/accessibilitylabel(__)-5r0pw.md>) — Adds a label to the chart content that describes its contents.
- [accessibilityLabel(_:)](<vectorizedchartcontent/accessibilitylabel(__)-8zoay.md>) — Adds a label to the chart content that describes its contents.
- [accessibilityLabel(_:)](<vectorizedchartcontent/accessibilitylabel(__)-46jbt.md>) — Adds a label to the chart content that describes its contents.
- [accessibilityValue(_:)](<vectorizedchartcontent/accessibilityvalue(__)-2rv8b.md>) — Adds a description of the value that the chart content contains.
- [accessibilityValue(_:)](<vectorizedchartcontent/accessibilityvalue(__)-pylk.md>) — Adds a description of the value that the chart content contains.
- [accessibilityValue(_:)](<vectorizedchartcontent/accessibilityvalue(__)-3dei8.md>) — Adds a description of the value that the chart content contains.

### Supporting types

- [PlottableProjection](plottableprojection.md)

### Associated Types

- [DataElement](vectorizedchartcontent/dataelement.md)

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
