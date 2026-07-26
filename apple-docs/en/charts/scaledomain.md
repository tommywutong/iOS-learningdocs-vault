---
title: ScaleDomain
framework: Swift Charts
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/charts/scaledomain
source_url: 'https://developer.apple.com/documentation/charts/scaledomain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/charts/scaledomain.json'
content_hash: 'sha256:e1829cc309464349'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Swift Charts](../charts.md)

# ScaleDomain

<sub>Protocol</sub>

A type that you can use to configure the domain of a chart.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
protocol ScaleDomain
```

## Overview

A type you use to configure the domain of a chart scale.

## Including zero in number scales

By default, number scales include zero in the domain to ensure charts follow the best practice to include a zero baseline in bar charts.

![](../../../attachments/e68dd25b1f8124a7a86dd5304dbae2b3/Scales.ChartWithDefaultCategoryDomain@2x.png)

<sub>Horizontal bar chart with y-axis showing categories A, B, and C and x-axis ranging from 0 to 15. There are three bars: A 5, B 10, C 15.</sub>

For other marks, this zero baseline isn’t as important, but the framework includes zero by default so the domain inference logic is consistent and deterministic.  Changing the mark type won’t suddenly affect scale domain.

![Horizontal dot plot with x-axis ranging from 0 to 100. It has 5 dots, at 12, 20, 50, 70, and 85.](../../../attachments/51bce47e24c398752082b540615e4812/ExNumberScale@2x.png)

If you don’t want to include the zero baseline in certain cases, use `automatic(includeszero:reversed:)` to customize the scale domain and disable the automatic zero inclusion.

```swift
Chart([20, 30, 50, 70, 85], id: \.self) {
    PointMark(
        x: .value("Value", $0)
    )
}
.chartXScale(domain: .automatic(includesZero: false))
```

![Horizontal dot plot with x-axis ranging from 20 to 100. It has 5 dots, at 20, 30, 50, 70, and 85.](../../../attachments/74790b460bf1b1cd57c6828ee5c8e922/ScaleDomain.ChartWithNumberScaleExcludingZero@2x.png)

## Reversing the order of inferred domain

You can also reverse the order of the inferred domain:

```swift
Chart([20, 30, 50, 70, 85], id: \.self) {
    PointMark(
        x: .value("Value", $0)
    )
}
.chartXScale(domain: .automatic(reversed: true))
```

![Horizontal dot plot with x-axis ranging from 100 to 0. It has 5 dots, at 85, 70, 50, 30, and 20.](../../../attachments/a3d2d262c008a7ac3df5f2215a9ba61d/ScaleDomain.ChartWithNumberScaleReversed@2x.png)

## Relationships

- **Conforming Types**: [AutomaticScaleDomain](automaticscaledomain.md)

## Topics

### Type Properties

- [automatic](scaledomain/automatic.md) — Creates a scale domain configuration that infers the scale domain from data.

### Type Methods

- [automatic(includesZero:reversed:)](<scaledomain/automatic(includeszero_reversed_).md>) — Creates a scale domain configuration that infers the scale domain from data.
- [automatic(includesZero:reversed:dataType:modifyInferredDomain:)](<scaledomain/automatic(includeszero_reversed_datatype_modifyinferreddomain_).md>) — Creates a scale domain configuration that infers the scale domain from data.

## See Also

### Scales

- [ScaleRange](scalerange.md) — A type that you can use to configure the range of a chart.
- [PositionScaleRange](positionscalerange.md) — A type that configures the x-axis and y-axis values.
- [PlotDimensionScaleRange](plotdimensionscalerange.md) — A range that represents the plot area’s width or height.
- [AutomaticScaleDomain](automaticscaledomain.md) — A domain that the chart infers from its data.
- [ScaleType](scaletype.md) — The ways you can scale the domain or range of a plot.
