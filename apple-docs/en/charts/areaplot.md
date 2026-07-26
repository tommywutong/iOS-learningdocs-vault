---
title: AreaPlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/areaplot
source_url: 'https://developer.apple.com/documentation/charts/areaplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/areaplot.json'
content_hash: 'sha256:e33c1439d7796105'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# AreaPlot

<sub>Structure</sub>

Chart content that represents a function or a collection of data using the area of one or more regions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AreaPlot<Content>
```

## Overview

Use `AreaPlot` when you want to visualize data in the same way as with [AreaMark](areamark.md), but you want to plot a function or visualize an entire data collection with a single plot.

### Plotting areas from a collection

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    AreaPlot(
        portfolioElements,
        x: .value("Date", \.date),
        y: .value("Asset value", \.assetValue),
        series: .value("Asset", \.asset),
        stacking: .standard
    )
    .foregroundStyle(by: .value("Asset", \.asset))
}
```

### Plotting functions

In addition to providing data points, you can provide a function to an `AreaPlot` to plot a function. For example, you can plot the area between y = x and y = x^2 - 1 with:

```swift
Chart {
    AreaPlot(x: "x", yStart: "x", yEnd: "x^2 - 1") { x in (yStart: x, yEnd: x * x - 1) }
}
.chartXScale(domain: -2 ... 2)
.chartYScale(domain: -4 ... 4)
```

You can also provide a single function to an `AreaPlot`. In this case it will plot the area between zero and the given function.

```swift
Chart {
    AreaPlot(x: "x", y: "x^2 - 1") { x in x * x - 1 }
}
.chartXScale(domain: -2 ... 2)
.chartYScale(domain: -4 ... 4)
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting areas from a collection

- [init(_:x:y:stacking:)](<areaplot/init(__x_y_stacking_).md>)
- [init(_:x:y:series:stacking:)](<areaplot/init(__x_y_series_stacking_).md>)
- [init(_:xStart:xEnd:y:)](<areaplot/init(__xstart_xend_y_).md>)
- [init(_:xStart:xEnd:y:series:)](<areaplot/init(__xstart_xend_y_series_).md>)
- [init(_:x:yStart:yEnd:)](<areaplot/init(__x_ystart_yend_).md>)
- [init(_:x:yStart:yEnd:series:)](<areaplot/init(__x_ystart_yend_series_).md>)

### Plotting functions

- [init(x:y:domain:function:)](<areaplot/init(x_y_domain_function_)-2fab1.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<areaplot/init(x_y_domain_function_)-1jmpp.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<areaplot/init(x_y_domain_function_)-etud.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:y:domain:function:)](<areaplot/init(x_y_domain_function_)-39eit.md>) — Creates a mark that fills the area between zero and the given function.
- [init(x:yStart:yEnd:domain:function:)](<areaplot/init(x_ystart_yend_domain_function_)-etcn.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x:yStart:yEnd:domain:function:)](<areaplot/init(x_ystart_yend_domain_function_)-9gui6.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x:yStart:yEnd:domain:function:)](<areaplot/init(x_ystart_yend_domain_function_)-5akqm.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).
- [init(x:yStart:yEnd:domain:function:)](<areaplot/init(x_ystart_yend_domain_function_)-23gxe.md>) — Creates a mark that fills the area between two functions (yStart, yEnd) = f(x).

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedAreaPlotContent](vectorizedareaplotcontent.md) — An opaque vectorized chart content type.
- [FunctionAreaPlotContent](functionareaplotcontent.md)

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [LinePlot](lineplot.md) — Chart content that represents a function or a collection of data using a sequence of connected line segments.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
