---
title: LinePlot
framework: Swift Charts
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/lineplot
source_url: 'https://developer.apple.com/documentation/charts/lineplot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/lineplot.json'
content_hash: 'sha256:3ce44accb1396ca2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# LinePlot

<sub>Structure</sub>

Chart content that represents a function or a collection of data using a sequence of connected line segments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct LinePlot<Content>
```

## Overview

Use `LinePlot` when you want to visualize data in the same way as with [LineMark](linemark.md), but you want to plot a function or visualize an entire data collection with a single plot.

### Plotting lines from a collection

You can initialize and style the plot with simple values or key paths. Add modifiers with `KeyPath` before adding modifiers with simple values.

```swift
Chart {
    LinePlot(
        stocks,
        x: .value("Date", \.date),
        y: .value("Price", \.price),
        series: .value("Asset", \.symbol)
    )
    .foregroundStyle(by: .value("Asset", \.symbol))
}
```

### Plotting functions

In addition to providing data points, you can provide a function to a `LinePlot` to plot a function. For example, you can plot the function y = x^2 with:

```swift
Chart {
    LinePlot(x: "x", y: "y") { x in x * x }
}
.chartXScale(domain: -10 ... 10)
.chartYScale(domain: -10 ... 10)
```

You can add multiple function plots in a chart and use different foreground styles to distinguish among them.

```swift
Chart {
    LinePlot(x: "x", y: "y = sin(x)") { sin($0) }
        .foregroundStyle(by: .value("expression", "y=sin(x)"))
        .lineStyle(StrokeStyle(lineWidth: 5, lineCap: .round))
        .opacity(0.8)

    LinePlot(x: "x", y: "y = cos(x)") { cos($0) }
        .foregroundStyle(by: .value("expression", "y=cos(x)"))
        .lineStyle(StrokeStyle(lineWidth: 5, lineCap: .round))
        .opacity(0.8)
}
.chartXScale(domain: -10 ... 10)
.chartYScale(domain: -10 ... 10)
```

You can plot a parametric function with the constructor with `x`, `y`, and `t`:

```swift
Chart {
    LinePlot(x: "x", y: "y", t: "t", domain: 0 ... .pi * 2) {
        t in (x: 10 * cos(5 * t) * cos(t), y: 10 * cos(5 * t) * sin(t))
    }
}
.chartXScale(domain: -10 ... 10)
.chartYScale(domain: -10 ... 10)
```

## Relationships

- **Conforms To**: [ChartContent](chartcontent.md), [Copyable](../swift/copyable.md), [Escapable](../swift/escapable.md), [VectorizedChartContent](vectorizedchartcontent.md)

## Topics

### Plotting lines from a collection

- [init(_:x:y:)](<lineplot/init(__x_y_).md>)
- [init(_:x:y:series:)](<lineplot/init(__x_y_series_).md>)

### Plotting functions

- [init(x:y:domain:function:)](<lineplot/init(x_y_domain_function_)-6m9gg.md>) — Creates a mark that graphs a function y = f(x).
- [init(x:y:domain:function:)](<lineplot/init(x_y_domain_function_)-1135f.md>) — Creates a mark that graphs a function y = f(x).
- [init(x:y:domain:function:)](<lineplot/init(x_y_domain_function_)-17i43.md>) — Creates a mark that graphs a function y = f(x).
- [init(x:y:domain:function:)](<lineplot/init(x_y_domain_function_)-6gv5v.md>) — Creates a mark that graphs a function y = f(x).

### Plotting parametric functions

- [init(x:y:t:domain:function:)](<lineplot/init(x_y_t_domain_function_)-5c4bo.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x:y:t:domain:function:)](<lineplot/init(x_y_t_domain_function_)-7bvyi.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x:y:t:domain:function:)](<lineplot/init(x_y_t_domain_function_)-610ta.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).
- [init(x:y:t:domain:function:)](<lineplot/init(x_y_t_domain_function_)-3mqls.md>) — Creates a mark that graphs a parametric function (x, y) = f(t).

### Supporting types

- [body](chartcontent/body-swift.property.md) — The content and behavior of the chart content.
- [VectorizedLinePlotContent](vectorizedlineplotcontent.md) — An opaque vectorized chart content type.
- [FunctionLinePlotContent](functionlineplotcontent.md)

## See Also

### Vectorized plots

- [Creating a data visualization dashboard with Swift Charts](creating-a-data-visualization-dashboard-with-swift-charts.md) — Visualize an entire data collection efficiently by instantiating a single vectorized plot in Swift Charts.
- [AreaPlot](areaplot.md) — Chart content that represents a function or a collection of data using the area of one or more regions.
- [PointPlot](pointplot.md) — Chart content that represents a collection of data using points.
- [RectanglePlot](rectangleplot.md) — Chart content that represents a collection of data using rectangles.
- [RulePlot](ruleplot.md) — Chart content that represents a collection of data using a single horizontal or vertical rule.
- [BarPlot](barplot.md) — Chart content that represents a collection of data using bars.
- [SectorPlot](sectorplot.md) — Chart content that represents a collection of data using a sector of a pie or donut chart, which shows how individual categories make up a meaningful total.
- [VectorizedChartContent](vectorizedchartcontent.md) — A generic type that represents content conveyed via a chart.
